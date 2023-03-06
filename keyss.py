#!/usr/bin/python

#Keys Screen

import Tkinter as Tk

#enable widget
class lfButton(Tk.LabelFrame):
  def __init__(self,parent=None, title="images", path="trees/", key='e', sx=4, sy=3, n=10):
    Tk.LabelFrame.__init__(self, parent,text=title)
    self.parent = parent
    self.enable=True
    self.init(path,key, sx,sy,n)
  #}__init__
  def init(self, path,key, sx,sy,n):
    self.pack(fill=Tk.X, padx=1, pady=1)
    self.parent.grid_rowconfigure(1,weight=1)
    self.parent.grid_columnconfigure(1,weight=1)
    ##enable
    bIm=Tk.Button(self
    , text='self'
    , command=self.enable_click
    )
    bIm.pack(side=Tk.LEFT)
    ##images
    self.path=path
    self.key=key
    self.sx=sx
    self.sy=sy
    self.n=n
    self.frame=fButton(self, path,key, sx,sy,n)
    self.frame.pack()
  #}init
  def enable_click(self):
    print(self.enable)
    self.enable=not(self.enable)
    if self.enable:
	  self.frame=fButton(self, self.path,self.key, self.sx,self.sy,self.n)
    else:
	  self.frame.pack_forget()
  #}enable_click
#}lfButton

#button widget
class fButton(Tk.Frame):
  def __init__(self,parent=None, path="trees/", key='e', sx=4, sy=3, n=10):
    Tk.Frame.__init__(self, parent)
    self.parent = parent
    self.key=key
    self.path=path
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
          self.imgs[y][x]=Tk.PhotoImage(file=self.path+self.key+'/f'+str(i+1)+'.png')
          self.bImg[y][x]=Tk.Button(self
          , text=self.key+'_image['+str(x)+','+str(y)+']'
          , image=self.imgs[y][x]
          , command= lambda x=x,y=y: self.button_click(x,y))
          self.bImg[y][x].grid(row=y,  column=x)
          self.keys[y][x]=self.key+' f'+str(i+1)
        else:
		  self.bImg[y][x]=None
		  self.imgs[y][x]=None
		  self.keys[y][x]=None
        i=i+1
  #}init
  def button_click(self,x,y):
    self.bImg[y][x].config(bg="green")
    print(self.keys[y][x], x,y)
  #}button_click
#}fButton

if __name__ == "__main__": 
  root=Tk.Tk()
  root.title("Image button window")
  #test
  def hide_me(event):
    event.widget.pack_forget()
  btn=Tk.Button(root, text="Click")
  btn.bind('<Button-1>', hide_me)
  btn.pack()
  btn2=Tk.Label(root, text="Click too")
  btn2.bind('<Button-1>', hide_me)
  btn2.pack()

  #button groups
  lfButton(root,"build","trees/scrin/", 'e',4,3,10)
  lfButton(root,"walk", "trees/scrin/", 'r',4,3,6)
  root.mainloop()
#}__main__
