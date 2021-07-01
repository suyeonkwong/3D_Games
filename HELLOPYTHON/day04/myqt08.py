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
        self.pb1.clicked.connect(self.clicked1)
        self.pb2.clicked.connect(self.clicked2)
        self.pb3.clicked.connect(self.clicked3)
        self.pb4.clicked.connect(self.clicked4)
        self.pb5.clicked.connect(self.clicked5)
        self.pb6.clicked.connect(self.clicked6)
        self.pb7.clicked.connect(self.clicked7)
        self.pb8.clicked.connect(self.clicked8)
        self.pb9.clicked.connect(self.clicked9)
        self.pb0.clicked.connect(self.clicked0)
        self.pb_call.clicked.connect(self.clickedpb_call)
        
    def clicked1(self):
        result = self.le.text()
        self.le.setText(result + "1")
        
    def clicked2(self):
        result = self.le.text()
        self.le.setText(result + "2")
        
    def clicked3(self):
        result = self.le.text()
        self.le.setText(result + "3")
        
    def clicked4(self):
        result = self.le.text()
        self.le.setText(result + "4")
        
    def clicked5(self):
        result = self.le.text()
        self.le.setText(result + "5") 
        
    def clicked6(self):
        result = self.le.text()
        self.le.setText(result + "6")  
        
    def clicked7(self):
        result = self.le.text()
        self.le.setText(result + "7")
        
    def clicked8(self):
        result = self.le.text()
        self.le.setText(result + "8") 
        
    def clicked9(self):
        result = self.le.text()
        self.le.setText(result + "9")
        
    def clicked0(self):
        result = self.le.text()
        self.le.setText(result + "0")
         
    def clickedpb_call(self):
        QMessageBox.about(self, "message", self.le.text())
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

