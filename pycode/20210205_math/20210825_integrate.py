
from sympy import *

# -------------------------------------------------------------------------------------
# name       : integrate_single()
# description: integrate one variable without low and up value, the function doesn't
#              create c constant.
#
#              integrate_single(func, var)
#
# date       : 20210825
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def integrate_single(_func, _x):
    result = integrate(_func, _x)
    print(">>> show integrate result: %s" % result)

# -------------------------------------------------------------------------------------
# name       : integrate_const_single()
# description: integrate one variable with low and up value
#
#              integrate_single(func, (var, low, up))
#
# date       : 20210825
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def integrate_const_single(_func, _x, _low, _up):
    result = integrate(_func, (_x, _low, _up))
    print(">>> show integrate constant result: %s" % result)

if __name__ == "__main__":
    x = symbols('x')
    y = symbols('y')
    l = symbols('l')

    # define function
    # x*e**(x*y)
    func_00 = x * exp(x * y)
    # e**(2*x)
    func_01 = exp(2*x)
    # 1 / (x*ln(x)*ln(ln(x)))
    func_02 = 1/(x*log(x)*log(log(x)))
    # 
    func_03 = (12*l**2*x+4*x**3)/(32*l**2)
    #integrate_single(func_02, x)
    low = 0
    up = l/2
    integrate_const_single(func_03, x, low, up)

