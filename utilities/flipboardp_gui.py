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

        # === 70/30 Split Layout ===
        self.log_frame = tk.Frame(self.root)
        self.log_frame.place(relx=0, rely=0, relwidth=0.7, relheight=1)

        self.right_frame = tk.Frame(self.root)
        self.right_frame.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


        # === Log Area (70% Frame) ===
        self.text = ScrolledText(self.log_frame, wrap='word', font=("Consolas", 9))
        self.text.pack(expand=True, fill='both')
        self.text.configure(state='disabled')

        # === Log Color Tags ===
        self.text.tag_config("normal", foreground="black")
        self.text.tag_config("success", foreground="green")
        self.text.tag_config("warning", foreground="orange")
        self.text.tag_config("error", foreground="red")
        self.text.tag_config("info", foreground="blue")

        # === Right Area (30% Frame) ===
        self.qr_label = tk.Label(self.right_frame)
        self.qr_label.pack(expand=True, fill='both')

        self.log(" FlipBoardP is running...", type="success")


# qr code generator
    def generate_qr(self, url: str):
        """
        Generates a QR from the given URL and displays it in the 30% right area.
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

        # Display the image in the right frame instead of text area
        self.qr_label.configure(image=tk_img)
        self.qr_label.image = tk_img  # Prevent GC


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