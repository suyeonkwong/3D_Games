import sys,time
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import socket
import threading

 
form_class = uic.loadUiType('myqt.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        self.client_socket.connect(('192.168.42.48', 9999))
      
        self.pb.clicked.connect(self.my_clicked)
        self.le.returnPressed.connect(self.my_clicked)
        
        my_t1 = threading.Thread(target=self.thread_recv)
        my_t1.start()
      
    def __del__(self):
        self.client_socket.close()
        
        
    def thread_recv(self):
        while True: 
            data = self.client_socket.recv(1024)
            str_new = repr(data.decode())
            str_new = str_new.replace("'", "")   
            str_old = self.te.toPlainText()
            txt = str_old + "\n" + str_new
            self.te.append(str_new)
            self.te.moveCursor(QtGui.QTextCursor.End)


        
    def my_clicked(self):
        message = self.le.text()
        txt = '{}:{}'.format(self.client_socket.getsockname()[0], message)
        self.client_socket.send(txt.encode())
        self.le.setText("")
        
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

