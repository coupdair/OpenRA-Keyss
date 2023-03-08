#!/usr/bin/python

#Keys Screen
#- v image   button window (root), i.e. Fn
#- v image trees, e.g. build=e (ertyu)
#- v zoom 2x for images
#- _ tooltip on checkbox/...
#- _ faction choice window, e.g. scrin/repear17
#- _ mods choice window, e.g. TD, RA, D, CA, ...

#metadata
__version__     = "0.1.2d"
__author__      = "Sebastien COUDERT" 

import Tkinter as Tk
import os
import tempfile
import string
import argparse

### CLI option ###
arg_zoom=1
arg_path="trees/scrin/"

parser = argparse.ArgumentParser(description='KeysScreen, i.e. RPI as HID keyboard.'
+ '(%(prog)s v'+__version__+')'
, epilog="examples: %(prog)s --help; %(prog)s --image-zoom=2"
)
##version
parser.add_argument('-v', '--version'
, action="store_true", default=False
, help='show version (default: False) currently v'+__version__)
##zoom
parser.add_argument('--image-zoom'
, default=arg_zoom
, help='zoom image factor, e.g. 2 (default: %(default)s).')
##path
parser.add_argument('--tree-path'
, default=arg_path
, help='path for directory trees (default: %(default)s).')

##parse
args=parser.parse_args()
version=args.version
arg_zoom=int(args.image_zoom)
arg_path=args.tree_path
###} CLI option ###

### GUI ###
#enable widget
class lfButton(Tk.LabelFrame):
  def __init__(self,parent=None, title="images", path="trees/", key='e', n=10, zoom=1, sx=4, sy=3):
    Tk.LabelFrame.__init__(self, parent,text=title)
    self.parent = parent
    self.init(path,key, sx,sy,n, zoom)
  #}__init__
  def init(self, path,key, sx,sy,n, zoom):
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
    self.frame=fButton(self, path,key, sx,sy,n, zoom)
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
  def __init__(self,parent=None, path="trees/", key='e', sx=4, sy=3, n=10, zoom=1):
    Tk.Frame.__init__(self, parent)
    self.parent = parent
    self.key=key
    self.path=path
    self.init(sx, sy, n, zoom)
  #}__init__
  def init(self, sx, sy, n, zoom):
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
          self.imgs[y][x]=self.imgs[y][x].zoom(zoom,zoom)
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
###} GUI ###

def dir_count(path):
  fp=tempfile.NamedTemporaryFile()
  cmd="ls "+path+" | wc -l > "+fp.name
  print(cmd)
  if( os.system(cmd)==0):
    line=fp.read()
  else:
    idle()
    return "directory list error"
  print(line)
  return int(line)
#}dir_count


if __name__ == "__main__": 
  root=Tk.Tk()
  root.title("Image button window")
  #button groups
  doGroup= ["build","shield","walk","vehicle","air"]#,"sea"]
  keyGroup=['e'    ,'r'     ,'t'   ,'y'      ,'u']#,'i']
  nbGroup= [10     ,7       ,6     ,8        ,5]
  #get image numbers
  for i in range(5) :
    nbGroup[i]=dir_count(arg_path+keyGroup[i]+'/')
  for i in range(5) :
    lfButton(root,doGroup[i],arg_path,keyGroup[i],nbGroup[i],arg_zoom)
  root.mainloop()
#}__main__

