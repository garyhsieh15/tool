
import os

# -------------------------------------------------------------------------------------
# name       : get_path_layer(_cur_dir)
# description: find all layer dir from near to far
#
# date       : 20210129
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def get_path_layer(_cur_dir):
    path_layer = []
    path_layer.append(_cur_dir)
    while os.path.basename(_cur_dir):
        _cur_dir = os.path.dirname(_cur_dir)
        path_layer.append(_cur_dir)

    path_layer.pop()
    return path_layer


def change_file_name():
    pass

def create_folder():
    pass

print(" ------------------------------------------------------------------------------ ")
cur_dir = os.getcwd()
print("cur_dir: ", cur_dir)
"""
cur_dir_split = os.path.split(cur_dir)
print("os.path.split(cur_dir): ", cur_dir_split)
print("os.path.split(cur_dir)[0]: ", cur_dir_split[0])
print("os.path.split(cur_dir)[1]: ", cur_dir_split[1])
print("type(cur_dir_split: ", type(cur_dir_split))

cur_dir_dirname = os.path.dirname(cur_dir)
print("os.path.dirname(cur_dir): ", cur_dir_dirname)

cur_dir_basename = os.path.basename(cur_dir)
print("os.path.dirname(cur_dir): ", cur_dir_basename)
"""
if __name__ == "__main__":
    # get current dir path
    cur_dir = os.getcwd()
    print("show path layer: ", get_path_layer(cur_dir))

