
import scipy as sp
import numpy as np

# -------------------------------------------------------------------------------------
# name       : calc_inverse(_A, _B)
# description: A * B = C, get B matrix.
#              a1x + b1y + c1z = d1
#              a2x + b2y + c2z = d2
#              a3x + b3y + c3z = d3
#
# date       : 20210205
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def calc_inverse(_A, _B):
    _C = np.linalg.solve(_A, _B)

    return _C


if __name__ == "__main__":
    A = sp.mat('[1 2 -5; 2 5 1; 2 3 8]')
    B = sp.mat('[10; -8; 5]')
    C = calc_inverse(A, B)
    print("show C matrix: ", C)

