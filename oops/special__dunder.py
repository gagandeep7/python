class Family:
    def __init__(self, fname, lname, relation, age):  # it is a type of default constructor
        self.fname = fname
        self.lname = lname
        self.relation = relation
        self.age = age

    def fullname(self):  # fuction for returning full name
        full = f"{self.fname} {self.lname}"
        return full

    def __add__(self, other):  # to get sum of ages of two objects
        return(self.age + other.age)

    def __str__(self):
        return 'Family("{}","{}","{}")'.format(self.fname, self.lname, self.relation)

    def __repr__(self):
        return '"{}","{}","{}"'.format(self.fname, self.lname, self.relation)
    


mom = Family("daljeet", "kaur", "mom", 50)  # mom is instance of class
gag = Family("gag", "singh", "cr7", 20)
# in this we use class name to call function so we need to pass instance of class
print(Family.fullname(mom))
print(mom.fullname())  # no need for parameter as it call itself
print(mom + gag)  # call __add__
print(mom.__add__(gag))  # specific calling
print(mom)  # calls str function as it is preferred more than repr
print(gag.__repr__())#calling repr individually
yes_votes =repr(42_572_654)
print(yes_votes[-1:-9:-1])# reverse the string 