from ursina import *
import tkinter as tk
from tkinter import messagebox
from sqlalchemy.sql.expression import false
 

arr2D = [
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
            ]
pb2D = []
flag_wb = [True]
flag_ing = [True]


app = Ursina()
# camera.orthographic = True
camera.z = -70

def myreset():
    print("myreset")
    #txt.visible = False
    flag_ing[0] = True
    flag_wb[0] = True
    for i in range(19):
        for j in range(19):
            arr2D[i][j] = 0
    myrender()
            
def myclose():
    print("myclose")
    txt_V.visible = False
    txt_V.enabled = False

Text.default_resolution = 1080 * Text.size
txt = Button(text='RESET', origin=(-6,-8), scale=(0.1,0.05,1), background=True,on_click=myreset)
txt_V = Button(text='victory', origin=(0,0), scale=(0.1,0.05,1), background=True,on_click=myclose,visible=False, enabled=False)



def myrender():
    for i in range(19):
        for j in range(19):
            if arr2D[i][j] == 0:
                pb2D[i][j].z = 0.7
            if arr2D[i][j] == 1:
                pb2D[i][j].z = -0.7
                pb2D[i][j].color = color.white
            if arr2D[i][j] == 2:
                pb2D[i][j].z = -0.7
                pb2D[i][j].color = color.black
                
                
def getUP(i,j,stone):
        
        cnt = 0
        try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
            while True:
                i += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
        
def getDW(i,j,stone):
        
        cnt = 0
        try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
            while True:
                i -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
def getRI(i,j,stone):
        
        cnt = 0
        try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
            while True:
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
def getLE(i,j,stone):
        
        cnt = 0
        try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
            while True:
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt            
        except:
            return cnt
        
def getUL(i,j,stone):
    
    cnt = 0
    try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
        while True:
            i += 1
            j += 1
            if i < 0 :
                return cnt
            if j < 0 :
                return cnt
            if arr2D[i][j] == stone:
                cnt += 1
            else:
                return cnt            
    except:
        return cnt
    
def getUR(i,j,stone):
    
    cnt = 0
    try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
        while True:
            i += 1
            j -= 1
            if i < 0 :
                return cnt
            if j < 0 :
                return cnt
            if arr2D[i][j] == stone:
                cnt += 1
            else:
                return cnt            
    except:
        return cnt
    
def getDL(i,j,stone):
    
    cnt = 0
    try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
        while True:
            i -= 1
            j += 1
            if i < 0 :
                return cnt
            if j < 0 :
                return cnt
            if arr2D[i][j] == stone:
                cnt += 1
            else:
                return cnt            
    except:
        return cnt
    
def getDR(i,j,stone):
    
    cnt = 0
    try: #바둑판 영역을 넘어서 돌놨을때 에러 처리
        while True:
            i -= 1
            j -= 1
            if i < 0 :
                return cnt
            if j < 0 :
                return cnt
            if arr2D[i][j] == stone:
                cnt += 1
            else:
                return cnt            
    except:
        return cnt

def myclick(i,j):
    print("myclick",i,j)
    if not flag_ing[0]:
        return
    
    if arr2D[i][j] > 0: #돌 있는 곳은 동작하지 않음
        return
    
    stone = -1
    if flag_wb[0]:
        arr2D[i][j] = 1
        stone = 1
        a = Audio(sound_file_name='baduk.mp3', pitch=1, loop=True, autoplay=True)
    else :
        arr2D[i][j] = 2
        stone = 2
        a = Audio(sound_file_name='baduk.mp3', pitch=1, loop=True, autoplay=True)
    
    
    up = getUP(i,j,stone)
    dw = getDW(i,j,stone)
    ri = getRI(i,j,stone)
    le = getLE(i,j,stone)
    
    ul = getUL(i,j,stone)
    ur = getUR(i,j,stone)
    dl = getDL(i,j,stone)
    dr = getDR(i,j,stone)
    
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
        
    myrender()
    
    
    if d1==5 or d2==5 or d3==5 or d4==5:
            if flag_wb[0] : 
                #messagebox.showinfo("Omok", "흰돌승리!!")
                #QtWidgets.QMessageBox.information("Omok", "흰돌")
                txt_V.text = "victory white"
                txt_V.visible = True
                txt_V.enabled = True
            else:
                #messagebox.showinfo("Omok", "흑돌승리!!")
                #QtWidgets.QMessageBox.information("Omok", "흑돌")
                txt_V.text = "victory balck"
                txt_V.visible = True
                txt_V.enabled = True
            flag_ing[0] = False
    
    flag_wb[0] = not flag_wb[0]
        
for i in range(20):
    line = []
    for j in range(20):
        pb = Entity(model='cube', texture='0',collider='box', on_click=Func(myclick, i,j))
        pb.x = j - 9
        pb.y = -i + 9
        
        sp = Entity(model='sphere', color=color.black, scale=(0.8,0.8,0.2))
        sp.z = 0.7
        sp.x = j - 9
        sp.y = -i + 9
        line.append(sp)
    pb2D.append(line)
    


def update():   # update gets automatically called.
    camera.rotation_z += held_keys['d'] * 1
    camera.rotation_z -= held_keys['a'] * 1
    
myrender()

app.run()   # opens a window and starts the game.