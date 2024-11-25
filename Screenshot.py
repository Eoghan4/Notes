import pyperclip, subprocess, time
from PIL import ImageGrab

def screenshot():
    pyperclip.copy("")
    subprocess.call(['explorer.exe', 'ms-screenclip:'])
    img = None
    while img is None:
        time.sleep(0.5)
        img = ImageGrab.grabclipboard()
    return img