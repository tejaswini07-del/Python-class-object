class Students:
    def _init_(self,n,a):
        self.name = n
        self.age = a
    
s1 = Students(1,'teju')
print(type(s1))
print(id(s1))

#HW TASK CREATE 5 CLASS AND 2 ATTRIBURS:
class Highway:
    def _init_(self,n,l):
        self.name =n
        self.length =l
    
s2 = Highway('National Highway','200km')
print(type(s2))
print(id(s2))

class fruit:
    def __init__(self,n,p):
        self.name = n
        self.price = p
s3 = fruit('apple','40km')  
print(type(s3))
print(id(s3))

class hotel:
    def __init__(self,n,m):
        self.name = n
        self.menu = m
s4 = hotel('hotel Maharaja','Menu')
print(type(s4))
print(id(s4))
        
class Doctor:
    def __init__(self,n,s):
        self.name = n
        self.specialization = s

s5 = Doctor('Dr.Jadhav','Cardiologist')
print(type(s5))
print(id(s5))

class hostel:
    def __init__(self,n,r):
        self.name  = n
        self.rent = r
        
s6 = hostel('Rutika',4000)
print(type(s6))
print(id(s6))
