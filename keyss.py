#!/usr/bin/python

#Keys Screen

import Tkinter as Tk

class fButton(Tk.Frame):
  def __init__(self,parent):
    Tk.Frame.__init__(self, parent)
    self.parent = parent
    self.initialize()

  def initialize(self):
    self.parent.title("Button frame")
    self.frame = Tk.Frame(self.parent)
    self.frame.pack(fill=Tk.X, padx=5, pady=5)
    self.parent.grid_rowconfigure(1,weight=1)
    self.parent.grid_columnconfigure(1,weight=1)
    sx=4
    sy=2
    self.bImg=[[0 for x in xrange(sx)] for x in xrange(sy)]
    for y in range(sy):
      for x in range(sx):
        self.bImg[y][x] = Tk.Button(self.frame, text = 'image['+str(x)+','+str(y)+']', command= lambda x=x,y=y: self.color_change(x,y))
        self.bImg[y][x].grid(row=y,  column=x)
  def color_change(self,x,y):
    self.bImg[y][x].config(bg="green")
    print x,y

if __name__ == "__main__": 
  root=Tk.Tk()
  fButton(root)  
  root.mainloop()
