class stud:
    def _init_(self,a,b,c):
        self.sno=a
        self.sname=b
        self.sage=c
    def display(self):
        print("student no:",self.sno)
        print("stunt name:",self.sname)
        print("student age:",self.sage)
        
x=int(input("Enter roll no:"))
y=input("Enter name:")
z=int(input("Enter age:"))
        
obj=stud(x,y,z)

