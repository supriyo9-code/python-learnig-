# def function1():
#     print("Subscribe Now")
# fun2 = function1
# del function1
# fun2()
# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a = funcret(0)
# print(a)
# def executor(func):
#     func("this")
# executor(print)
def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexec()

@dec1
def who_is_Supriyo():
    print("Supriyo is a good boy")
#who_is_Supriyo=dec1(who_is_Supriyo)
who_is_Supriyo