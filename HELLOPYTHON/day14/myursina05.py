from ursina import *
app= Ursina()
class Option(Button):
  def __init__(self):
    super().__init__(
      model= 'circle',
      texture= 'brick',
      color= color.blue,
      scale= 0.3)
    
  #def on_click():
  #  doSomething()
demo_button= Option()
app.run()
