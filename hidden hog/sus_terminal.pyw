import os
import sys
import ctypes
import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound
import time
import random

def display_window():
    root = tk.Tk()
    root.title("Alert")
    root.geometry("1366x768")

    image_path = "daemon.png"
    image = Image.open(image_path)
    image_tk = ImageTk.PhotoImage(image)

    canvas = tk.Canvas(root, width=1366, height=768)
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)

    def play_sound_and_close_window():
        playsound("toggle.wav")
        root.destroy()

    display_time = 1.5
    root.after(int(display_time * 1000), play_sound_and_close_window)
    root.update()
    root.attributes("-topmost", True)
    root.mainloop()

def change_wallpaper(image_path):
    if sys.platform.startswith('win'):
        SPI_SETDESKWALLPAPER = 0x0014
        SPIF_UPDATEINIFILE = 0x01
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE)
    elif sys.platform.startswith('darwin'):
        script = f'tell application "Finder" to set desktop picture to POSIX file "{image_path}"'
        os.system(f'osascript -e \'{script}\'')
    elif sys.platform.startswith('linux'):
        os.system(f'gsettings set org.gnome.desktop.background picture-uri file://{image_path}')

if len(sys.argv) < 2:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, 'daemon.png')
else:
    image_path = sys.argv[1]

while True:
    time.sleep(random.randint(21600, 28800))
    display_window()
    change_wallpaper(image_path)
