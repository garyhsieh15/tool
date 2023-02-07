

class MyCalClass:
    class_var = 15

    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1

    def calc_add1(self, a, b):
        self.__calc_add1()
        return a + b

    def calc_add2(self):
        return self.x + self.y

    def calc_mutli(self, a, b):
        print("calc_add2: ", self.calc_add2())
        return a * b

    def calc_print(self, a):
        print("a value:", a)
        print("self.y value:", self.y)

    def __calc_add1(self):
        print("__calc_add1")

    def using_member_var(self):
        print("show self.class_var:", self.class_var)
        print("show self.calc_add2();", self.calc_add2())

def show_me_the_money():
    print("enter show me the money")

class_ex_a = 11


if __name__ == "__main__":

    instance_1 = MyCalClass(1, 2)
    instance_2 = MyCalClass(5, 10)

    print("instance_1.calc_add1:", instance_1.calc_add1(5, 3))
    print("instance_1.calc_add2:", instance_1.calc_add2())
    print("instance_1.mutli:", instance_1.calc_mutli(2, 4))
    instance_1.calc_print(5)
    print("instance_1.x, instance_2.y: ", instance_1.x, instance_2.y)
    print("MyCalClass.class_var: ", MyCalClass.class_var)
    MyCalClass.class_var = 22
    print("MyCalClass.class_var: ", MyCalClass.class_var)
    
    print("-------------------------------------------")
    print("instance_1.class_var: ", instance_1.class_var)
    #instance_1.class_var = 33
    #instance_2.class_var = 333
    print("instance_1.class_var: ", instance_1.class_var)
    print("instance_2.clsaa_var: ", instance_2.class_var)

    print("-------------------------------------------")
    MyCalClass.class_var = 555
    print("instance_1.class_var: ", instance_1.class_var)
    print("instance_2.clsaa_var: ", instance_2.class_var)
    print("MyCalClass.class_var: ", MyCalClass.class_var)

    print("-------------------------------------------")
    instance_1.using_member_var()
