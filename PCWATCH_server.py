import socket

from os import getlogin

from PIL import Image
import io
import numpy as np
from random import randint
import pyautogui
# Поток
from threading import Thread
# PyQt5
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QAction, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect, Qt

#hostt__name is misspelled on purpose
hostt__name = socket.gethostname()
IP_addres = socket.gethostbyname(hostt__name)
#width = int(input("Width Of Screen (720 reccommended): "))
#height = int(input("Height Of Screen (1280 reccommended): "))
width = 720
height = 1280
a = '192.168.0.136'
if a == '':
    pass
else:
    IP_addres = a
print(f"[!] STARTED | RESOLUTION: {height} X {width}")
IP_port = 8080
print(f"[!] IP ADDRESS: [localhost] // PORT {IP_port}")
sock = socket.socket()
sock.bind((IP_addres, IP_port))
sock.listen()
conn, addr = sock.accept()

class Desktop(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def ChangeImage(self):
        try:
            print("[!] CONNECTED".format(addr[0]))
            while True:
                img_bytes = conn.recv(9999999)
                self.pixmap.loadFromData(img_bytes)
                self.label.setScaledContents(True)
                #self.label.resize(self.width(), self.height())
                self.label.resize(height, width)
                self.label.setPixmap(self.pixmap)
        except ConnectionResetError:
            QMessageBox.about(self, "ERROR", "The remote host forcibly terminated the existing connection")
            conn.close()
        except:
            pass
            conn.close()

    def initUI(self):
        self.pixmap = QPixmap()
        self.label = QLabel(self)
        #self.label.resize(self.width(), self.height())
        self.label.resize(height, width)
        self.setGeometry(QRect(pyautogui.size()[0] // 4, pyautogui.size()[1] // 4, 800, 450))
        #self.setFixedSize(self.width(), self.height())
        self.label.resize(height, width)
        self.setWindowTitle("[PCWATCH] Watching Desktop: " + addr[0])
        self.start = Thread(target=self.ChangeImage, daemon=True)
        self.start.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Desktop()
    ex.resize(height, width)
    ex.show()
    sys.exit(app.exec())
