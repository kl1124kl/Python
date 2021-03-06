##Author: Jiaqi Li
## Date: 11/13/2018
class Auto:
    def __init__(self,m = '',y=1900,c=''):
        self.__make = m
        self.__year = y
        self.__color = c

    def get_year(self):
        return self.__year

    def __str__(self):
        return self.__make + " from " + str(self.__year) + " is " + self.__color
class Truck(Auto):
    #inheriting the attributes from the class Auto
    def __init__(self,m='',y=1900,c='',d=''):
##        self.__make = m
##        self.__year = y
##        self.__color = c
##        self.__drive = d
#instead of doing the above, we can do:
        Auto.__init__(self,m,y,c)
        self.__drive = d #overriden the constructor, the child class is more specific than the parent class

    def get_drive(self):
        return self.__drive
        
    def __str__(self):
        return Auto.__str__(self)+' with ' + self.__drive #overrides the str method from the auto class 

lists_of_car = []
lists_of_car.append(Auto('ford',2016,'blue'))
#the object my_car has the type called Auto
lists_of_car.append(Auto('Tesla',2018,'red'))
lists_of_car.append(Auto('GM',2008,'white'))
lists_of_car.append(Auto('Volkswagon',1998,'brown'))
lists_of_car.append(Truck('Ford F100',2010,'black','4WD'))
print(lists_of_car[-1].get_drive())
for cars in lists_of_car:
    if isinstance(cars,Truck):#if the car is an instance of the class Truck
        print(cars.get_year())
    else:
        print(cars.get_year())
my_truck = Truck('Ford F100',2010,'black','4WD')
print(my_truck)
#the truck class inherited the str method from the auto class
print(my_truck.get_drive())
#the parent class can not use the moethod that only exists in the child class
