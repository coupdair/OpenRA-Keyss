#!/usr/bin/python

#Keys Screen

import Tkinter as Tk

#button window
class fButton(Tk.Frame):
  def __init__(self,parent=None, sx=4, sy=2, n=6):
    Tk.Frame.__init__(self, parent)
    self.parent = parent
    self.init(sx, sy, n)
  #}__init__
  def init(self, sx, sy, n):
    self.parent.title("Button frame")
    self.pack(fill=Tk.X, padx=5, pady=5)
    self.parent.grid_rowconfigure(1,weight=1)
    self.parent.grid_columnconfigure(1,weight=1)
    self.bImg=[[0 for x in xrange(sx)] for x in xrange(sy)]
    i=0
    for y in range(sy):
      for x in range(sx):
        self.bImg[y][x]=Tk.Button(self, text='image['+str(x)+','+str(y)+']', command= lambda x=x,y=y: self.button_click(x,y))
        self.bImg[y][x].grid(row=y,  column=x)
        if i>n-1:
		  self.bImg[y][x].config(bg="red")
        i=i+1
  #}init
  def button_click(self,x,y):
    self.bImg[y][x].config(bg="green")
    print(x,y)
  #}button_click

if __name__ == "__main__": 
  root=Tk.Tk()
  fButton(root)
  root.mainloop()
#}__main__
