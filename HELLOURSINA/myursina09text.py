from ursina import *
app = Ursina()

def myreset():
    
    print("myreset")
    txt.visible = False

Text.default_resolution = 1080 * Text.size
txt = Button(text='RESET', origin=(-6,-8), scale=(0.1,0.05,1), background=True,on_click=myreset())


def update():
    camera.rotation_z += held_keys['d'] * 1
    camera.rotation_z -= held_keys['a'] * 1
    

app.run()