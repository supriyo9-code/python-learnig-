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

    def __add__(self,other):
            return self.salary+other.salary

    def __truediv__(self, other):
        return self.salary / other.salary
    def __repr__(self):
        return f"Employee('(self,name)',(self.salary),'(self.role)')"
    def __str__(self):
        return f"The Name is {self.name}.Salary is {self.salary}.and role is {self.role}"

emp1 =Employee("Harry", 345, "Programmer")
#emp2 =Employee("Rohan", 85, "Cleaner")
print(str(emp1))