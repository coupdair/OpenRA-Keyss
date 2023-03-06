#!/usr/bin/python

#Keys Screen

import Tkinter as Tk

#button window
class fButton(Tk.LabelFrame):
  def __init__(self,parent=None, title="images", key='e', sx=4, sy=3, n=10):
    Tk.LabelFrame.__init__(self, parent,text=title)
    self.parent = parent
    self.key=key
    self.init(sx, sy, n)
  #}__init__
  def init(self, sx, sy, n):
    self.pack(fill=Tk.X, padx=5, pady=5)
    self.parent.grid_rowconfigure(1,weight=1)
    self.parent.grid_columnconfigure(1,weight=1)
    self.bImg=[[0 for x in xrange(sx)] for x in xrange(sy)]
    self.imgs=[[0 for x in xrange(sx)] for x in xrange(sy)]
    self.keys=[[0 for x in xrange(sx)] for x in xrange(sy)]
    i=0
    for y in range(sy):
      for x in range(sx):
        if i<n:
          self.imgs[y][x]=Tk.PhotoImage(file='tux.png')
          self.bImg[y][x]=Tk.Button(self
          , text=self.key+'_image['+str(x)+','+str(y)+']'
          , image=self.imgs[y][x]
          , command= lambda x=x,y=y: self.button_click(x,y))
          self.bImg[y][x].grid(row=y,  column=x)
          self.keys[y][x]=self.key+' f'+str(i+1)
        else:
		  self.bImg[y][x]=None
		  self.keys[y][x]=None
        i=i+1
  #}init
  def button_click(self,x,y):
    self.bImg[y][x].config(bg="green")
    print(self.keys[y][x], x,y)
  #}button_click

if __name__ == "__main__": 
  root=Tk.Tk()
  root.title("Image button window")

  image0=Tk.PhotoImage(file='tux.png')
  bImg0=Tk.Button(root
  , text='root'
  , image=image0
  , command= lambda: exit()
  )
  bImg0.pack()#side=Tk.LEFT)

  image1=Tk.PhotoImage(file='tux.png')
  bImg1=Tk.Button(root
  , text='root'
  , command= lambda: exit()
  )
  bImg1.config(image=image1)
  bImg1.pack()#side=Tk.RIGHT)
  
  fButton(root)
  fButton(root,"others",'r',4,2,7)
  root.mainloop()
#}__main__
