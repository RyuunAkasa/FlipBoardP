import pyperclip
import time
import datetime
import json

class ClipboardManager:

    def __init__(self , visual_update,history_saving_file_path='history.txt'):

        self.visual_update = visual_update
        self.clipboard_data = ""
        self.history_saving_file_path = history_saving_file_path
        self.history_serial = 1 #used to organise the history numberwise
        



    def watch_pc_clipboard(self):
       
        self.visual_update.log("Watching PC clipboard for changes...", "info")
        last_clipboard = self.clipboard_data
        while True:
            try:
                current = pyperclip.paste()
                if current != last_clipboard:              
                    self.clipboard_data = last_clipboard = current

                    preview = current[:50] + ".." if len(current) > 50 else current
                    self.visual_update.log(f"Last Clipboard data: {preview}", "info")

                    self.save(current,self.history_saving_file_path)

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


    def save(self,data,file_path):

        try:
            with open(file_path,'a') as history_file:
                data = f'{self.history_serial}. - {datetime.datetime.now()} - {data}\n\n'
                if history_file.write(data) == len(data):
                    self.visual_update.log('Saved to clipboard history.','info')
                    self.history_serial +=1
                    return True
                else:
                    self.visual_update.log('Failed to save clipboard data!','warning')
        except Exception as e:
            print(e)
            self.visual_update.log('Error occured while saving clipboard data!','error')

        
        return False