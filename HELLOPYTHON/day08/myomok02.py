import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from sqlalchemy.sql.expression import false

 
form_class = uic.loadUiType('myomok02.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.arr2D = [
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0]
            ]
        
        self.pb2D = []
        self.flag_wb = True
        self.flag_ing = True
        self.setupUi(self)
        
        self.pb_reset.clicked.connect(self.myreset)
       
        for i in range(10): 
            line = []
            for j in range(10):
                pb1 = QPushButton(self)
                pb1.setText('')
                pb1.setIconSize(QSize(40, 40)) #아이콘사이즈
                pb1.setToolTip("{},{}".format(i,j))
                pb1.setGeometry(j*40,i*40,40,40) #버튼사이즈
                pb1.setIcon(QtGui.QIcon('0.png'))
                pb1.clicked.connect(self.my_clicked)
                line.append(pb1)
            self.pb2D.append(line)
        self.myrender()
            
     
    def myreset(self):
        self.flag_ing = True
        self.flag_wb = True
        for i in range(10):
            for j in range(10):
                self.arr2D[i][j]=0
        self.myrender()
            
    def myrender(self):
        for i in range(10): 
            for j in range(10):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
                    
                    
    def my_clicked(self):
        if not self.flag_ing:
            return
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j] > 0: #돌 있는 곳은 동작하지 않음
            return
        
        stone = -1
        
        if self.flag_wb:
            self.arr2D[i][j] = 1
            stone = 1
        else:
            self.arr2D[i][j] = 2
            stone = 2
    
        up = self.getUP(i,j,stone)
        dw = self.getDW(i,j,stone)
        ri = self.getRI(i,j,stone)
        le = self.getLE(i,j,stone)
        
        ul = self.getUL(i,j,stone)
        ur = self.getUR(i,j,stone)
        dl = self.getDL(i,j,stone)
        dr = self.getDR(i,j,stone)
        
        print("up",up)
        print("dw",dw)
        print("ri",ri)
        print("le",le)
        print("ul",ul)
        print("ur",ur)
        print("dl",dl)
        print("dr",dr)
            
            
        d1 = up + dw + 1
        d2 = ur + dl + 1
        d3 = le + ri + 1
        d4 = dr + ul + 1
        
        self.myrender()
        if d1==5 or d2==5 or d3==5 or d4==5:
            if self.flag_wb : 
                QtWidgets.QMessageBox.information(self, "Omok", "흰돌")
            else:
                QtWidgets.QMessageBox.information(self, "Omok", "흑돌")
            self.flag_ing = False
        self.flag_wb = not self.flag_wb
        
    def getUP(self,i,j,stone):
        
        cnt = 0
        
        try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
            while True:
                i += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
            
    def getDW(self,i,j,stone):
        
        cnt = 0
        try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
            while True:
                i -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
    def getRI(self,i,j,stone):
        
        cnt = 0
        try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
            while True:
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
    def getLE(self,i,j,stone):
        
        cnt = 0
        try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
            while True:
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
    def getUL(self,i,j,stone):
        
        cnt = 0
        try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
            while True:
                i += 1
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
    def getUR(self,i,j,stone):
        
        cnt = 0
        try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
            while True:
                i += 1
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
    def getDL(self,i,j,stone):
        
        cnt = 0
        try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
            while True:
                i -= 1
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
    def getDR(self,i,j,stone):
        
        cnt = 0
        try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
            while True:
                i -= 1
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
                
    
    
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

