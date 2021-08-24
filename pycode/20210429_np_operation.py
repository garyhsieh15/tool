
import numpy as np

# -------------------------------------------------------------------------------------
# name       : create_np_array()
# description: create matrix via np.array() function.
#

# date       : 20210429
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def create_np_array():
    _a = np.array([1, 2, 3, 4, 5, 6])
    print("_a array matrix: \n", _a)

# -------------------------------------------------------------------------------------
# name       : create_arange()
# description: create matrix via arange() function.
#

# date       : 20210429
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def create_arange():
    _a = np.arange(0, 20)
    print("a arange matrix: \n", _a)

    return _a

def change_shape(_matrix):
    a = _matrix.reshape(2, 10)
    print(" _matrix: \n", _matrix)
    print(" a: \n", a)

    return a

# -------------------------------------------------------------------------------------
# name       : modify_melement()
# description: modify element of matrix.
#              np.where(condition, x, y), if condition is right, then x or y.
#
# date       : 20210429
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def modify_melement(_matrix):
    nm = np.where(_matrix % 2 == 0, 0, 1)
    nm_01 = np.where(nm != 0, 3, nm)
    print("after matrix: \n", nm)
    print("after matrix: \n", nm_01)

# -------------------------------------------------------------------------------------
# name       : melement_max()
# description: find max element of matrix.
#              np.amax(matrix, axis = 0 or 1)
#
# date       : 20210429
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def melement_max():
    _a = np.array([[1, 3, 2],
        [4, 1, 8],
        [9, 6, 7]])
    print("_a matrix: \n", _a)
    print("np.amax(_a, axis = 0): \n", np.amax(_a, axis = 0))
    print("np.amax(_a, axis = 1): \n", np.amax(_a, axis = 1))

# -------------------------------------------------------------------------------------
# name       : melement_min()
# description: find min element of matrix.
#              np.amin(matrix, axis = 0 or 1)
#
# date       : 20210429
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def melement_min():
    _a = np.array([[[1, 3, 2],
        [4, 1, 8],
        [9, 6, 7]],
        [[2, 1, 2],
            [3, 4, 3],
            [5, 9, 1]]])
    print("_a matrix: \n", _a)
    print("np.amin(_a, axis = 0): \n", np.amin(_a, axis = 0))
    print("np.amin(_a, axis = 0, keepdims = True): \n", np.amin(_a, axis = 0, keepdims = True))
    print("np.amin(_a, axis = 1): \n", np.amin(_a, axis = 1))
    print("np.amin(_a, axis = 1, keepdims = True): \n", np.amin(_a, axis = 1, keepdims = True))
    print("np.amin(_a, axis = 2): \n", np.amin(_a, axis = 2))
    print("np.amin(_a, axis = 2, keepdims = True): \n", np.amin(_a, axis = 2, keepdims = True))

# -------------------------------------------------------------------------------------
# name       : init_random_matrix()
# description: create initial and random matrix.
#              np.random.randinit(num, size)
#
# date       : 20210429
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def int_random_matrix():
    _a = np.random.randint(20, size=(4, 5))
    print("_a random and init: \n", _a)
 
if __name__ == "__main__":
    print("enter main func")

    #a = create_arange()
    #aa = create_np_array()
    #b = change_shape(a)
    #modify_melement(b)
    #melement_max()
    #melement_min()
    int_random_matrix()
