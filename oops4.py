class Employee:
    no_of_mobile =10
    def __init__(self, aname,asalary,arole):
        self.name= aname
        self.salary= asalary
        self.role= arole

    def printdetails(self):
        return f"The Name is {self.name}.Salary is {self.salary}.and role is {self.role}"
    @classmethod
    def change_mobile(cls,newbobile):
        cls.no_of_mobile=newbobile

Supriyo = Employee("Supriyo ", 10000, "Student")
Roumita = Employee("Roumita", 100000, "SDE")

Roumita.change_mobile(100)
print(Roumita.no_of_mobile)