
# OK.
#from package import module_test as mt
# OK. 
#from package.module_test import MyCalClass
# OK.
#from package.module_test import class_ex_a
# OK.
#from package.module_test import show_me_the_money
# NG
#from package.module_test.show_me_the_money
# NG
#from package import *
# OK.
#from package.module_test import *
# OK.
#import package.module_test
# NG. 
#import package.module_test.MyCalClass

# 以下測試同層的*.py
# OK. 
#from class_module import class_ex_a
# NG.
import class_module.class_ex_a


#print("mt.MyCalClass.class_var: ", mt.MyCalClass.class_var)
#print("MyCalClass.class_var: ", MyCalClass.class_var)
#print("class_ex_a: ", class_ex_a)
#show_me_the_money()

#print("MyCalClass.class_var: ", MyCalClass.class_var)

#print("package.module_test.MyCalClass.class_var: ", package.module_test.MyCalClass.class_var)
#print("package.module_test.MyCalClass.class_var: ", package.module_test.MyCalClass.class_var)
#print("MyCalClass.class_var: ", MyCalClass.class_var)
#print("class_var: ", class_ex_a)
print("class_module.class_ex_a: ", class_module.class_ex_a)

