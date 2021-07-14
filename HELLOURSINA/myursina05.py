from ursina import *

app = Ursina()

def myclick(str):
    print("myclick",str)
    
    
player = Entity(model='cube', texture='0',collider='box', on_click=Func(myclick, '0,0'))


def update():   # update gets automatically called.
    camera.rotation_z += held_keys['d'] * 1
    camera.rotation_z -= held_keys['a'] * 1
    
    

app.run()   # opens a window and starts the game.