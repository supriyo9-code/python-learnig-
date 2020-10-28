class Employee:
    no_of_mobile =10
    def __init__(self, aname,asalary,arole):
        self.name= aname
        self.salary= asalary
        self.role= arole

    def printdetails(self):
        return f"The Name is {self.name}.Salary is {self.salary}.and role is {self.role}"


Supriyo = Employee("Supriyo ", 10000, "Student")
# Roumita = Employee()
#
# Supriyo.name ="Supriyo"
# Supriyo.salary = 10000
# Supriyo.role = "student"
#
# Roumita.name = "Roumita"
# Roumita.salary =1000000
# Roumita.role = "SDE"
print(Supriyo.salary)