class Dad:
    basketball = 1

class Son:
    dance=1
    basketball = 9
    def isdance(self):
       return f"yes i dance {self.dance} no of times"

class Grandson:
    dance = 6
    guiter = 1

    def isdance(self):
        return f"Jackson yeha!" \
               f"yes i dance very awesomely {self.dance} no of dance"

Darry = Dad()
Larry = Son()
Harrry = Grandson()
print(Harrry.isdance())