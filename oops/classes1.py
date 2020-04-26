class Family:
    def __init__(self,fname,lname,relation,age):#it is a type of default constructor
        self.fname=fname
        self.lname=lname
        self.relation=relation
        self.age=age
    def fullname(self):# fuction for returning full name
        full=f"{self.fname} {self.lname}"
        return full
mom=Family("daljeet","kaur","mom",50)#mom is instance of class
print(Family.fullname(mom))#in this we use class name to call function so we need to pass instance of class
print(mom.fullname())#no need for parameter as it call itself
