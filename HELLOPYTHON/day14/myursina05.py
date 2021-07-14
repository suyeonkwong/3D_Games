from ursina import *

app = Ursina()

def myclick():
    print("myclick")

player = Entity(model='Circle', color=color.white, scale=(1,0.1,1))

b = Button(text='hello world!', color=color.azure, icon='0.png', scale=.25, text_origin=(-.5,0))
b.on_click = myclick # assign a function to the button.
b.tooltip = Tooltip('exit')


def update():   # update gets automatically called.
    player.x += held_keys['d'] * 1
    player.x -= held_keys['a'] * 1

app.run()   # opens a window and starts the game.
