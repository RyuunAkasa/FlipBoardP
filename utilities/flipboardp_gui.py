from PIL import Image, ImageTk
import qrcode
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import io

class FlipBoardGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("FlipBoardP")

        window_width = 300
        window_height = 100
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = screen_width - window_width - 10
        y = screen_height - window_height - 50
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")


        self.root.resizable(False,False)
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.7)



        # === Log Area ===
        self.text = ScrolledText(self.root, wrap='word', font=("Consolas", 9), height=7)
        self.text.pack(expand=False, fill='both')
        self.text.configure(state='disabled')

        # === Log Color Tags ===
        self.text.tag_config("normal", foreground="black")
        self.text.tag_config("success", foreground="green")
        self.text.tag_config("warning", foreground="orange")
        self.text.tag_config("error", foreground="red")
        self.text.tag_config("info", foreground="blue")

        self.log(" FlipBoardP is running...", type="success")






# qr code generator
    def generate_qr(self, url: str):
        """
        Generates a QR from the given URL and embeds it inside the log area.
        """
        qr = qrcode.QRCode(box_size=2, border=1)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert to Tkinter-compatible image
        with io.BytesIO() as buffer:
            img.save(buffer, format="PNG")
            buffer.seek(0)
            image = Image.open(buffer)
            tk_img = ImageTk.PhotoImage(image)

        label = tk.Label(self.text, image=tk_img)
        label.image = tk_img  # Prevent GC
        self.text.configure(state='normal')
        self.text.insert('end', '\n')  # Line break
        self.text.window_create('end', window=label)
        self.text.insert('end', '\n')  # Optional line after QR
        self.text.configure(state='disabled')




# Showing logs text
    def log(self, message, type="normal"):
        """
        Log function takes in two parameters - message and its type 
        - type is like a color code for special situations, for example there are 5 types of message type you can pass on. Deafult type is normal which shows black text in color.
        - "success", color is "green" | "warning", color is "orange" | "error", color is "red" | "info", color is "blue" | "normal", color is "black"
        """

        self.text.configure(state='normal')
        self.text.insert('end', f"{message}\n", type)
        self.text.see('end')
        self.text.configure(state='disabled')





    def start(self):
        self.root.mainloop()
