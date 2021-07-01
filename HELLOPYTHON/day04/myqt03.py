import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets

 
form_class = uic.loadUiType('myqt02.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.my_clicked)
    
        
    def my_clicked(self):
        a = int(self.lbl.text())
        a += 1
        self.lbl.setText(str(a))
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

