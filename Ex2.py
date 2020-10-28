print("what do you want to do? +,-,*,/")
func1=input()
print("enter first number")
num1=int(input())
print("enter second number")
num2=int(input())

if num1==45 and num2==3 and func1=='*':
    print("555")
elif num1==56 and num2==9 and func1=='+':
    print("77")
elif num1==56 and num2==6 and func1=='/':
    print("4")
elif func1=='+':
    addition=num1+num2
    print(addition)
elif func1=='*':
    multiplication =num1*num2
    print(multiplication)
elif func1=='/':
    division=num1/num2
    print(division)
elif func1=='-':
    substraction=num1-num2
    print(substraction)
else:
    print("go to hell")