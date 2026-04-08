import pyperclip
import time


class ClipboardManager:

    def __init__(self , visual_update):

        self.visual_update = visual_update
        self.clipboard_data = ""


    def watch_pc_clipboard(self):
       
        self.visual_update.log("Watching PC clipboard for changes...", "warning")
        last_clipboard = self.clipboard_data
        while True:
            try:
                current = pyperclip.paste()
                if current != last_clipboard:              
                    self.clipboard_data = last_clipboard = current

                    preview = current[:50] + ".." if len(current) > 50 else current
                    self.visual_update.log(f"Last Clipboard data: {preview}", "info")

            except Exception as e:
                self.visual_update.log(f"Clipboard read error: {e}", "error")

            # Refresh timer
            time.sleep(.5)





    def compare_and_update(self,new_data):
             
        if new_data.strip() != self.clipboard_data.strip():

                self.clipboard_data = new_data
                pyperclip.copy(new_data)
                self.visual_update.log(f" Clipboard updated from Device: {new_data}", "success")


        else:
            self.visual_update.log(f" Device tried to update clipboard with same data", "warning")

