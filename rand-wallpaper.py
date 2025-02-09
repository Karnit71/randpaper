import random
import os

path = "/path/to/folder" #your path to folder with wallpapers 
dir = os.listdir (path)
ran = random.randrange (1,len(dir))
com = 'gsettings set org.cinnamon.desktop.background picture-uri "file://' + path + "/" + str(dir[ran]) + '"'
os.system (com)
os.system ("echo " + str (dir [ran]))
