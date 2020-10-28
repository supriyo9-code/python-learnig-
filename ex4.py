# Parttern parinting
print("How Many Row You Want To Print")
# one = int(input())
# print("Type 1 or 0")
# two = int(input())
# new = bool(two)
# if new==True:
#     for i in range(1,one+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#             print()
# elif new == False:
#     for i in range (one,0,-1):
#         for j in range(1,i+1):
#             print("*",end="")
#             print()
print("pattern printing")
num=int(input("Enter how may row you want: "))
print("Enter 1 or 0")
bool_val = input("1 for True value or 0 for False : ")
if bool_val=="1":
    for i in range (0,num+1):
        print("*"*int(i))
if bool_val=="0":
    for i in range(num,0,-1):
        print("*"*int(i))
