#!/usr/bin/python

#Keys Screen
#- v image   button window (root), i.e. Fn
#- v image trees, e.g. build=e (ertyu)
#- _ tooltip on checkbox/...
#- _ faction choice window, e.g. scrin/repear17
#- _ mods choice window, e.g. TD, RA, D, CA, ...

import Tkinter as Tk
import os
import tempfile
import string

#enable widget
class lfButton(Tk.LabelFrame):
  def __init__(self,parent=None, title="images", path="trees/", key='e', n=10, sx=4, sy=3):
    Tk.LabelFrame.__init__(self, parent,text=title)
    self.parent = parent
    self.init(path,key, sx,sy,n)
  #}__init__
  def init(self, path,key, sx,sy,n):
    self.pack(fill=Tk.X, padx=1, pady=1)
    self.parent.grid_rowconfigure(1,weight=1)
    self.parent.grid_columnconfigure(1,weight=1)
    ##enable
    self.vEnable=Tk.IntVar()
    self.vEnable.set(True)
    cb=Tk.Checkbutton(self, text='',variable=self.vEnable, onvalue=True, offvalue=False, command=self.cbEvent)
    cb.pack(side=Tk.LEFT)
    ##images
    self.path=path
    self.key=key
    self.sx=sx
    self.sy=sy
    self.n=n
    self.frame=fButton(self, path,key, sx,sy,n)
    self.frame.pack()
  #}init
  def cbEvent(self):
    if (self.vEnable.get()==True):
      self.frame=fButton(self, self.path,self.key, self.sx,self.sy,self.n)
    else:
      self.frame.pack_forget()
  #}cbEvent
#}lfButton

def keyssend(keyss):
  fp=tempfile.NamedTemporaryFile()
  cmd="~/pizero-usb-hid-keyboard/sendkeys "+keyss+" > "+fp.name
  print(cmd)
  if( os.system(cmd)==0):
    line=fp.read()
  else:
    idle()
    return "usb-hid-keyboard/sendkeys error"
  print(line)
  return line
#}keyssend

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
    keyssend(self.keys[y][x])
    print(self.keys[y][x], x,y)
  #}button_click
#}fButton

if __name__ == "__main__": 
  root=Tk.Tk()
  root.title("Image button window")
  #button groups
  lfButton(root,"build",   "trees/scrin/", 'e',10)
  lfButton(root,"shield",  "trees/scrin/", 'r',7)
  lfButton(root,"walk",    "trees/scrin/", 't',6)
  lfButton(root,"vehicle", "trees/scrin/", 'y',8)
  lfButton(root,"air",     "trees/scrin/", 'u',5)
  root.mainloop()
#}__main__
