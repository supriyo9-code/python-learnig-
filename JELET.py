print("what is your GMR?")
GMR = int(input())
if GMR<=50:
    print("you can get any govt collge")
elif GMR>50 and GMR<=100:
    print("you get  govt college but chances of ju is less")
elif GMR>100 and GMR<=200:
    print("you can get govt college excluding JU")
elif GMR>200 and GMR<=500:
    print("you can get govt college excludig ju,kgec,jgec")
elif GMR>500 and GMR<=10000:
    print("You only get a good private college")
else:
    print("better luck next time")
