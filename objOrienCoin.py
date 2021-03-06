#Author: Jiaqi Li
#10/30/2018
class Coin:
    #use __init__ to create new object of the class 
    def __init__(self,n='Penny',s='head'):
    #these are default values 
#create a default coin
        #use self to keep track of which one is which
        self.__value = 0
        self.__name = n
        self.__side = s
        self.__check_value()
#double underscore protects the attributes,cant be accessed outside, the only way to
        #access them is through setter and getter
        #by using self, python can tell the differences between defferent objects we created,every time we have (), type self first
    def get_name(self):
        return self.__name
    def get_value(self):
        return self.__value
    def set_coin(self,n,s=None):
##        self.__value = v
        self.__name = n
        if s != None:
            self.__side = s
        self.__check_value()
#this is a hiddened method
    def __check_value(self):
        #this is a private constant
        #make a dictionary
        __VALUE = {'penny' : 1, 'nickle' : 5, 'dime' : 10, 'quarter': 25}
        if self.__name not in __VALUE:
            #check if it is in the dictionary
            self.__name = 'penny'
        self.__value = __VALUE[self.__name]#this will return the value associated with the name
            #use str method when we want to print all the info about the objects
    #return a boolean, allows us to compare two objects
    def __lt__(self,other):
        lt = self.__value < other.__value #this is a boolean
        return lt

    def __str__(self):
      return self.__name +' ' + str(self.__value) + ' ' + self.__side
        
coin1 = Coin()
coin1.set_coin(10,'head')#this is how we change the attributes of the object
##print(coin1.get_name())#this is the classic way to access a protected information from an object or a method
coin2 = Coin()
##print(coin2.get_name())
#create a new coin
coin3 = Coin('nickle','tails')
##print(coin3.get_name())

coin4 = Coin('quarter','tails')
##print(coin4.get_name())
##print(coin4.get_value())

##coin3 = coin2
list_coins = [coin1,coin2,coin3,coin4]
for coins in list_coins:
    ##    print(coins.get_name())
    print(coins)
list_coins.sort()

for coins in list_coins:
    print(coins)
if coin1 < coin2:
    print("less than")
else:
    print("greater")

#the sort method can't be used to sort objects, it only works for numbers

## we can now use the __str__ method to print the coins, instead of using the getter and then the print statement.
    
## naming convention in python, the class name should begin with an upper case letter and the variable should begin with a
    #lower case letter
    ## any constant's name should be all caps.
    
