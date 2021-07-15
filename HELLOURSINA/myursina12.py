from ursina import *

app = Ursina()
camera.y = 30
camera.z= 0
camera.rotation_x = 90


for i in range(10):
    for j in range(10):
        temp = Entity(model='cube',texture="0", color=color.orange)
        temp.z = 4.5 - i
        temp.x = -4.5 + j
        


def update():   # update gets automatically called.
    camera.rotation_y = camera.rotation_y+1
  
app.run()   # opens a window and starts the game.