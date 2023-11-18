from tkinter import Tk, Canvas, ARC, W, CENTER
from human import Human


class Hero(Human):

    def __init__(self, canvas, x, y, name, gen):
        super().__init__(canvas, x, y, name, gen)
        self._health = 100
        
    def _drawName(self):
        name = f"{self._name.split()[0]} {self._name.split()[1][0]}. {self._name.split()[2][0]}."
        #self.canvas.create_text(20, 390, text=name, justify=CENTER, font="Verdana 14")
        #self.canvas.create_line(self.x+200, 200, self.x+300, 200, width=3)
        self.canvas.create_rectangle(self.x,self.y-250,self.x+100, self.y-230, fill='red', outline='black', width=3)
            
             
        if self.gen=='м':
            self.canvas.create_line(self.x, self.y-100, self.x-100, self.y-200)
            self.canvas.create_line(self.x-30, self.y-100, self.x, self.y-130)
        else:
            self.canvas.create_arc(self.x, self.y-150, self.x+100, self.y-50, start=-240, extent=160, style=ARC, outline='darkblue', width=5)
        
            