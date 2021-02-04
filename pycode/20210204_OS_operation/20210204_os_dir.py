
import os


PATH = "./pic/"

# -------------------------------------------------------------------------------------
# name       : modify_file_name(_path)
# description: modify all *.jpg file name from 0 to N.
#
# date       : 20210204
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def modify_file_name(_path):
    
    xfiles = os.listdir(_path)
    i = 0
    for xfile_name in xfiles:
        ext = xfile_name.split('.')
        #print("file_name and ext info: ", file_name, ext)
        
        if ext[-1] == "jpg":
            os.rename(_path + xfile_name, _path +  str(i) + "__.jpg")
            i = i + 1
    
    yfiles = os.listdir(_path)
    j = 0
    for yfile_name in yfiles:
        ext = yfile_name.split('.')
        if ext[-1] == "jpg":
            os.rename(_path + yfile_name, _path + str(j) + ".jpg")
            j = j + 1

if __name__ == "__main__":
    path = PATH #"./pic/"
    modify_file_name(path)
