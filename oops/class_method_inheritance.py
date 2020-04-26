import datetime
class Employee:
    amount=1.04

    def __init__(self,fname,lname,salary):#it is a type of default constructor
        self.fname=fname
        self.lname=lname
        self.salary=int(salary*self.amount)
    def full(self):    #regular or instance method
        nn= (self.fname+" " +self.lname)
        return nn
    @classmethod
    def string(cls,emp):
        fname,lname,salary=emp.split('-')
        return cls(fname,lname,int(salary))
    @staticmethod
    def iswork(day):
        	if day.weekday == 5 or  day.weekday() == 6 :
        		return False
        	return True	


class developer(Employee):#inheritance from employee class
    def __init__(self, fname, lname,salary,lang):
        super().__init__(fname,lname,salary)#from empoloyeee class
        self.lang=f"best {lang}"
class manager(Employee):  # inheritance from employee class
        def __init__(self, fname, lname, salary,employees=None):
            super().__init__(fname, lname, salary)#  from employee class
            if employees is None:
                self.employees=[]
            else:
                self.employees=employees
        def add_emp(self,emp):
            if emp not in self.employees:
                self.employees.append(emp)
        def rmv_emp(self,emp):
            if emp  in self.employees:
                self.employees.remove(emp)
        def print_emp(self):
            for emp in self.employees:
                print(emp.full())



data='gagan-deep-5000'#string
emp1=Employee.string(data)#string spilting

print(emp1.fname,emp1.lname,emp1.salary)#call class method
print(emp1.full())#call instance method
print(isinstance(developer,Employee))#tell whether a class is inherited or not also issubclass can be used
dev1=developer("siraj","raval",10000,"python")#create developer instance with addition of prog language
print(dev1.lang)
mng1=manager("elon","musk",100000,)#mnager intance with employes list
print(mng1.employees)
mng1.print_emp()#intialy no employees
mng1.add_emp(dev1)#devloper added
mng1.add_emp(emp1)#new employee added
mng1.print_emp()
print(mng1.__dict__)
mng1.rmv_emp(dev1)# remove developer from manager contact
mng1.print_emp()
dt=datetime.date(2019,6,23)
print(emp1.iswork(dt))# static method call