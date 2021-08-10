
class MyCalClass:
    class_var = 11

    def __init__(self, x1, y1, var):
        self.x = x1
        self.y = y1
        self.class_var = var

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

def show_me_the_money():
    print("enter show me the money")

class_ex_a = 11

if __name__ == "__main__":
    instance_1 = MyCalClass(1, 2, 111)
    instance_2 = MyCalClass(5, 10, 111)

    print("instance_1.calc_add1:", instance_1.calc_add1(5, 3))
    print("instance_1.calc_add2:", instance_1.calc_add2())
    print("instance_1.mutli:", instance_1.calc_mutli(2, 4))
    instance_1.calc_print(5)
    print("instance_1.x, instance_2.y: ", instance_1.x, instance_2.y)
    print("MyCalClass.class_var: ", MyCalClass.class_var)
    print("instance_1.class_var: ", instance_1.class_var)
    MyCalClass.class_var = 22
    instance_1.class_var = 222
    print("after modify MyCalClass.class_var: ", MyCalClass.class_var)
    print("after modify instance_1.class_var: ", instance_1.class_var)


