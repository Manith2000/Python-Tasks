import os


'c:\\desktop\\coding' #remember to do double \\ for windows since  \ python is an escape OR write as raw string

p = os.path.join('f1','f2','f3','code.png')
print(p) #os module prints this using appropriate notation depending on your OS

print(os.getcwd()) #get current work directory

#os.chdir('c:\\') this changes directory to c 

#os.path.abspath('x.png') this converts to find absolute path
#os.path.isabs() this checks if absolute file path
#os.path.relpath('x.png') this converts to find relative path
#os.path.dirname
#os.path.basename
#os.path.exists()
#os.path.isfile()
#os.path.isdir()
#os.path.getsize()
#os.listdir()
#os.makedirs()
#os.walk() allow syou to walk through an entire folder and its contents for processing



#use shelve module to handle data and store in binary files
#this works similar ot dictionaries with keys & values

#use shutil module to copy/move/delete files & folders
#use send2trash module from pip to send files/folders to recycling bin