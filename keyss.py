#!/usr/bin/python

#Keys Screen

import Tkinter as Tk

#button window
class fButton(Tk.LabelFrame):
  def __init__(self,parent=None, title="images", sx=4, sy=2, n=6):
    Tk.LabelFrame.__init__(self, parent,text=title)
    self.parent = parent
    self.init(sx, sy, n)
  #}__init__
  def init(self, sx, sy, n):
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
		  self.bImg[y][x]["state"] = "disabled"
        i=i+1
  #}init
  def button_click(self,x,y):
    self.bImg[y][x].config(bg="green")
    print(x,y)
  #}button_click

if __name__ == "__main__": 
  root=Tk.Tk()
  root.title("Button frame")
  fButton(root)
  fButton(root,"others",4,2,7)
  root.mainloop()
#}__main__
