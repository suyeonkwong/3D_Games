import sys,time
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import threading

 
form_class = uic.loadUiType('myqt_messinger_th_o.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.my_clicked)
        
        
    def myfunc_th(self):
        print("myfunc_th")
        #for i in range(5):
        #    time.sleep(1)
        #    a = self.lbl.text()
        #    int_a = int(a)
        #    int_a += 1
        #    self.lbl.setText(str(int_a))
     
    def my_clicked(self):
        #my_t1 = threading.Thread(target=self.myfunc_th)
        #my_t1.start()
        for i in range(5):
            time.sleep(1)
            a = self.lbl.text()
            int_a = int(a)
            int_a += 1
            self.lbl.setText(str(int_a))
        
                
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

