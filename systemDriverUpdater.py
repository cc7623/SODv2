from time import sleep

while True:
    import ctypes
    ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\image.PNG", 0)

    sleep(5)

