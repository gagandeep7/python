class Family:
    cast="aujla"# it is class variable and common for all
    def __init__(self,fname,lname,relation,age):#it is a type of default constructor
        self.fname=fname
        self.lname=lname
        self.relation=relation
        self.age=age

    def fullname(self):# fuction for returning full name
        nn=f"{self.fname} {self.lname} {self.cast}"
        return nn
    @classmethod
    def setcast(cls,cast):
    	cls.cast=cast
            
mom=Family("daljeet","kaur","mom",50)#mom is instance of class
print(Family.fullname(mom))#in this we use class name to call function so we need to pass instance of class
print(mom.fullname())#no need for parameter as it call itself
print(mom.__dict__)
mom.cast="atwal"#changing class variable value for particular person(only change for mom attribute)
mom.setcast="atwal"# instance can aldso be use to call class method
print(mom.cast)
print(mom.setcast)# it is same as mom.cast
gag=Family(fname="gagandeep",lname="singh",relation="myself",age=20)
print(gag.cast)# here global value remain same
intial=gag.cast# storing intial global value
Family.cast="raval"# changing global value
siraj=Family("siraj","ml","scientist",25)
print(siraj.fullname())
print("intial global value",intial.upper(),"changed object value",mom.cast.upper(),"global value changed",Family.cast.upper())