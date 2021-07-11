import os


#PATH = "./pic/"
#PATH = "/Volumes/TOSHIBA_EXT/work/NCKU/10902/dl/HW01/images/images/bear/train_bear/"
#PATH = "/Volumes/TOSHIBA_EXT/work/NCKU/10902/dl/HW01/images/images/bear/test_bear/"
#PATH = "/Volumes/TOSHIBA_EXT/work/NCKU/10902/dl/HW01/images/images/leopard/train_leopard/"
PATH = "/Volumes/TOSHIBA_EXT/work/NCKU/10902/dl/HW01/images/images/leopard/test_leopard/"
# -------------------------------------------------------------------------------------
# name       : modify_file_name(_path)
# description: modify all *.jpg file name from 0 to N.
#
# date       : 20210204
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def modify_file_name(_path):
    
    xfiles = os.listdir(_path)
    print("show xfiles: ", xfiles)
    i = 0
    for xfile_name in xfiles:
        ext = xfile_name.split('.')
        print("file_name and ext info: ", xfile_name, ext)
         
        #if ext[-1] == "jpg":
        if ext[-1] == "JPEG" and ext[0] != "":
            #os.rename(_path + xfile_name, _path +  str(i) + "__.jpg")
            os.rename(_path + xfile_name, _path +  str(i) + "__.JPEG")
            i = i + 1
        
    
    yfiles = os.listdir(_path)
    j = 0
    for yfile_name in yfiles:
        ext = yfile_name.split('.')
        #if ext[-1] == "jpg":
        if ext[-1] == "JPEG" and ext[0] != "":
            #os.rename(_path + yfile_name, _path + str(j) + ".jpg")
            os.rename(_path + yfile_name, _path + str(j) + "_leopard.JPEG")
            j = j + 1

if __name__ == "__main__":
    path = PATH #"./pic/"
    modify_file_name(path)
