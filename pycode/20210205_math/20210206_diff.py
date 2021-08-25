
from sympy import *

"""
d(sinx) / dx -> cosx
d(cosx) / dx -> -sinx
d(tanx) / dx -> sec ** 2x
d(cotx) / dx -> −csc ** 2x
d(secx) / dx -> secxtanx
d(cscx) / dx -> secxtanx
"""
# -------------------------------------------------------------------------------------
# name       : diff_basic
# description: differential for Trigonometric function
#
#              diff(func(var), var)
#
# date       : 20210206
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def diff_basic_tri():

    x = symbols('x')
    diff_sin = diff(sin(x), x)
    diff_cos = diff(cos(x), x)
    diff_tan = diff(tan(x), x)
    diff_cot = diff(cot(x), x)
    diff_sec = diff(sec(x), x)
    diff_csc = diff(csc(x), x)

    print("show diff sinx =  %20s" % ( diff_sin))
    print("show diff cosx =  %20s" % ( diff_cos))
    print("show diff tanx =  %20s" % ( diff_tan))
    print("show diff cotx =  %20s" % ( diff_cot))
    print("show diff secx =  %20s" % ( diff_sec))
    print("show diff cscx =  %20s" % ( diff_csc))

# -------------------------------------------------------------------------------------
# name       : partial_diff()
# description: partial differential for x*e ** (x*y)
#
#              diff(func(var), var)
#
# date       : 20210206
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def partial_diff(_func, _x):
    partial_diff = diff(_func, _x)
    print("show partial diff( x * e ** x*y ) = %s" % (partial_diff))


if __name__ == "__main__":
    x = symbols('x')
    y = symbols('y')
    
    # define function
    func_00 = x * exp(x * y)
    func_01 = exp(x)
    #partial_diff(func, x)

