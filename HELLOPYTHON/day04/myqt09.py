import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from random import random
from PyQt5.QtWidgets import QMessageBox

 
form_class = uic.loadUiType('myqt09.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.clicked)
        self.pb2.clicked.connect(self.clicked)
        self.pb3.clicked.connect(self.clicked)
        self.pb4.clicked.connect(self.clicked)
        self.pb5.clicked.connect(self.clicked)
        self.pb6.clicked.connect(self.clicked)
        self.pb7.clicked.connect(self.clicked)
        self.pb8.clicked.connect(self.clicked)
        self.pb9.clicked.connect(self.clicked)
        self.pb0.clicked.connect(self.clicked)
        self.pb_call.clicked.connect(self.clickedpb_call)
        
    def clicked(self):
        str_old = self.le.text()
        str_new = self.sender().text()
        self.le.setText(str_old+str_new)
        
    def clickedpb_call(self):
        #QMessageBox.about(self, "message", self.le.text())
        
        tel = self.le.text()
        QtWidgets.QMessageBox.information(self, "Telephone", "calling" + tel)
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

