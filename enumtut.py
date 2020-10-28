#Without Enumerate Functiion
l1 =["Bhindi","Aloo","Chopsticks","Chowmean"]
# i=1
# for item in l1:
#     if i%2 != 0:
#         print(f"Jarvis please bye {item}")
#     i+=1
#With Enumerate Function
for index, item in enumerate(l1):
    if index%2 == 0:
        print(f"Jarvis please bye {item}")

