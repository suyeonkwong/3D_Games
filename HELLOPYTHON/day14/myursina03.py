from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(-5,5,0))
player = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(0,5,0))
player = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(5,5,0))
player = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(-5,0,0))
player = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(0,0,0))
player = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(5,0,0))
player = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(-5,-5,0))
player = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(0,-5,0))
player = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(5,-5,0))

camera.z = -30

def update():   # update gets automatically called.
    player.x += held_keys['d'] * 1
    player.x -= held_keys['a'] * 1

app.run()   # opens a window and starts the game.
