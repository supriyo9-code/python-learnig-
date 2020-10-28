#list = [["supriyo",1], ["swaraj",2], ["debraj",4], ["loknath",6]]
#dict1 = dict(list)
#print(dict1)
#for item, fish in dict1.items():
  #  print(item,"and fish is",fish)
items = [int ,float,"supriyo",6,4,5,22,56,45,65,35,15]
for item in items:
    if str(item).isnumeric() and item >= 6:
        print(item) 