import os
import pickle

FILE_NAME = "test.pkl"


# -------------------------------------------------------------------------------------
# name       : rw_binary_file(_path)
# description: write binary file then read binary file.
#
# date       : 20210422
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def rw_binary_file(_path):
    my_list = [1, 2, 3]
    print("show raw file: ", my_list)

    
    #write binary file
    pickle_file = open(path + "/" + FILE_NAME,'wb')
    pickle.dump(my_list,pickle_file)

    pickle_file.close()

    # read binary file
    pickle_file = open(path + "/" + FILE_NAME,'rb')
    my_list2 = pickle.load(pickle_file)
    print("show binary file: ", my_list2)

    pickle_file.close()


if __name__ == "__main__":
    print("---- enter main func ----")
    path = os.getcwd()
    print("show path: ", path)

    rw_binary_file(path)
