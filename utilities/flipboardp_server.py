from flask import Flask, request
import socket
import threading

class MiniServer:
    def __init__(self, visual_update, clipboard_manager_class_object,token_mode = False,token_text = ""):
        self.visual_update = visual_update
        self.clipboard = clipboard_manager_class_object

        self.app = Flask(__name__)
        self.token_mode = token_mode
        self.token_text = token_text

        # Register routes dynamically here
        self.app.add_url_rule("/clipboard", view_func=self.send_data, methods=["GET"])
        self.app.add_url_rule("/clipboard", view_func=self.recieve_data, methods=["POST"])




# This shows local ip 
# It creates a UDP socket and connects to 8.8.8.8 to determine which local IP address would be used.
# Then it returns that local IP without sending any actual data.
    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        self.visual_update.log("Trying to get local ip through Google DNS", "warning")
        ip = s.getsockname()[0]
        s.close()
        return ip



# This function here  checks for token as well as sends data to devices
    def send_data(self):

        token = request.args.get("token")

        self.visual_update.log(" Device requested clipboard", "warning")

        if self.token_mode and token != self.token_text:
            self.visual_update.log(" Unautorized device detected", "error")
            return "Unauthorized is strictly access is prohibited", 401
        
        self.visual_update.log(" Device request fulfilled", "success")
        return self.clipboard.clipboard_data, 200



# This function checks for token as well as recieve data from the device 
    def recieve_data(self):

        token = request.args.get("token")

        if self.token_mode and token != self.token_text:
            self.visual_update.log(" Unautorized device tried to post", "error")
            return "Unauthorized is strictly access is prohibited", 401
        try:
            new_data = request.data.decode("utf-8")
            self.clipboard.compare_and_update(new_data=new_data)
            return "OK", 200
        except Exception as e:
            self.visual_update.log(f" Error updating clipboard: {e}", "error")
            return "ERROR", 500



#runs the server and check for any clipboard update only if token values are not mismatched
    def run_server(self):

        if self.token_mode and len(self.token_text.strip())<1 :

            self.visual_update.log("Token mode and Token text value mismatch!"+
                                "\n Restart the app with correct values!","error")
        
            
        else:
            ip = self.get_local_ip()
            arguments = ""
            if self.token_mode : arguments = f"?token={self.token_text}"
            url = f"http://{ip}:5000/clipboard{arguments}"
            self.visual_update.log(f"IP- {url}", "success")
            self.visual_update.generate_qr(url)
            
            threading.Thread(target=self.clipboard.watch_pc_clipboard, daemon=True).start()
            self.app.run(host="0.0.0.0", port=5000)





