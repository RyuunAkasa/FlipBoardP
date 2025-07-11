from utilities.flipboardp_gui import FlipBoardGUI as fpgui
from utilities.flipboardp_clipboard_manager import ClipboardManager as clpm
from utilities.flipboardp_server import MiniServer as msv
import threading
import os
from dotenv import load_dotenv


visual_update = fpgui()

clipboard = clpm(visual_update = visual_update)

# Can be added token text(by deafult its empty string) and turn on or off the mode(by default its False) 
# for a lil bit of sequrity to prevent someone send or recieve the data
# Explicitly load 'token.env' from the utilities directory

load_dotenv(dotenv_path="token.env")
token_mode = os.getenv("TOKEN_MODE", "False") == "True"
token_text = os.getenv("TOKEN_TEXT", "")


server = msv(visual_update = visual_update
             ,clipboard_manager_class_object = clipboard,
             token_mode = token_mode,
             token_text=token_text)


# Run the server , cliboard bg watcher , gui on different threads 

if __name__ == "__main__":
    
    threading.Thread(target=server.run_server, daemon=True).start()
    visual_update.start()
