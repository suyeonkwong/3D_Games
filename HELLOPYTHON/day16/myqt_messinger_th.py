import sys,time
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep

 
form_class = uic.loadUiType('myqt_messinger_th.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.my_clicked)
        self.le.returnPressed.connect(self.my_clicked)
        
        for i in range(5):
            time.sleep(1)
            self.my_clicked2(str(i))
            
        
        
    def my_clicked2(self,a):
        str_old = self.te.toPlainText()
        str_new = a
        txt = str_old + "\n" + str_new
        
        self.te.setPlainText(txt)
        self.le.setText("")
        self.te.moveCursor(QtGui.QTextCursor.End)
        
        
    def my_clicked(self):
        for i in range(5):
            time.sleep(1)
            self.my_clicked2(str(i))
        

                
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

