import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from random import random

 
form_class = uic.loadUiType('myqt07.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.my_clicked)
        self.le_mine.returnPressed.connect(self.myenter)
        
    def myenter(self):
        self.doGame()
        
    def my_clicked(self):
        
        self.doGame()
                        
 
    def doGame(self):
        
        mine = self.le_mine.text()
        comp = ""
        result = ""
        
        rnd = random()
        if rnd > 0.5 :
            comp = "홀"
        else :
            comp = "짝"
        
         
        if mine == comp :
            result = "승리"
        else :
            result = "패배"
        
        self.le_com.setText(comp)
        self.le_result.setText(result)
            
            
 
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

