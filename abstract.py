from abc import abstractmethod

class Emp:
    @abstractmethod
    def Daysalary(self,hr,r):
        pass
    @abstractmethod
    def Monthsal(self,m):
        pass
    @abstractmethod
    def Absentsal(self,x):
        pass
    @abstractmethod
    def Tax(self,t):
        pass

class Engineer(Emp):
    def Daysalary(self, hr, r):
        global day
        day = hr*r
        print(day)
    def Monthsal(self, m):
        global month
        month = day*m
        print(month)
    def Absentsal(self, x):
        global ab
        ab = day*x
        print(ab)
    def Tax(self, t):
        global tax
        tax = month*t/100
        print(tax)
    def Totalsal(self):
        total = month-ab-tax
        print(total)

k= Engineer()
k.Daysalary(7,2500)
k.Monthsal(30)
k.Absentsal(4)
k.Tax(5)
k.Totalsal()
