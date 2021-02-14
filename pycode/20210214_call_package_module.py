#from package import class_package
from package.class_package import MyCalClass

#import class_module




if __name__ == "__main__":
    # test package
    """
    instance_1 = class_package.MyCalClass(1, 2)
    print("instance_1.calc_add1:", instance_1.calc_add1(5, 3))
    """
    
    # test module
    """
    instance_1 = class_module.MyCalClass(1, 2)
    print("instance_1.calc_add1:", instance_1.calc_add1(5, 3))

    class_module.show_me_the_money()
    print("show class_moduel.class_ex_a: ", class_module.class_ex_a)
    """
    # test package.module
    instance_1 = MyCalClass(1, 2)
    print("instance_1.calc_add1:", instance_1.calc_add1(5, 3))

