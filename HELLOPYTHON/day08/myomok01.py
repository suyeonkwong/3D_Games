import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

 
form_class = uic.loadUiType('myomok01.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.idx = 0
        self.setupUi(self)
        self.pb.clicked.connect(self.my_clicked)
        
        
    def my_clicked(self):
        self.idx += 1
        namuji = self.idx % 3
        self.pb.setIcon(QtGui.QIcon('{}.png'.format(namuji)))
        
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

