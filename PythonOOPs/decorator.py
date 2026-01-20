class Employee:
    empCount = 0

    def __init__(self,name , age):
        self.name = name 
        self.age = age 
        Employee.empCount +=1

        @classmethod
        def showcount(cls):
             print(cls.empCount)

        @classmethod
        def newemployee(cls , name, age):
             return cls(name,age)

e1= Employee("Bhavanaa",24)
e2= Employee("Ram",23)
e3= Employee("Anil",21)