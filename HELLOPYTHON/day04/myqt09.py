import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from random import random

 
form_class = uic.loadUiType('myqt08.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.my_clicked)
        
    def my_clicked(self):
        print("1")
        mine = ""
        comp = ""
        result = ""
        print("2")
        rnd = random()
        if rnd > 0.66 :
            comp = "가위"
        elif rnd > 0.33:
            comp = "바위"
        else :
            comp = "보"
        print("3")
        self.le_com.setText(comp)
        print("4")
        mine = self.le_mine.text()
        
        if mine=="가위" and comp=="보" or mine=="바위" and comp=="가위" or mine=="보" and comp=="바위":
            result = "승리"
        elif mine == comp:
            result = "비김"
        else :
            result = "패배"
            
        self.le_result.setText(result)
                        
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

