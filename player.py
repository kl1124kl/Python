__AUTHOR_NAME__ = "Jiaqi Li"
import math
class Player:
    #the constructor takes in three parameters, and make them private so that they are can only be accessed
    #outside of the class through getters.
    def __init__(self, name = '', character='', items=[]):
        self.__name = name
        self.__character = character
        self.__list_item = items
    
    def __str__(self):
        return self.__name,self.__character, self.__list_item

    def getName(self):
        return self.__name
    
    def getClass(self):
        return self.__character
    
    def get_list(self):
        return self.__list_item
    
    def getCharacter(self):
        return self.__character
    
    def getItems(self):
        return self.__list_item
#The parameter is an empty list by default
    def add(self,my_list=[]):
        for item in my_list:
            self.__list_item.append(item)

#The parameter is an empty list by default, only remove the first occurence of the parameter list in self.__list_item
    def remove_item(self, my_list = []):
        for item in my_list:
            if item in self.__list_item:
                self.__list_item.remove(item)
#The parameter is an empty list by default, remove every occurence of the parameter list in self.__list_item
    def removeAll(self,item = []):
        for e in self.__list_item:
            for el in item:
                if e == el:
                    self.__list_item.remove(e)
        

#Parameter item1 and item2 are type of string by default
    def replaceItem(self, item1='', item2=''):
        if item1 in self.__list_item:
            item1 = item2

    def changeClass(self, new_character):
        self.__character = new_character
    
#Compare parameter player's list and the original list, if player's list have the same variables as self.__list_item, return true
    def compareItems(self, player2):
        for items in player2.get_list():
            if items in self.__list_item:
                return True
            else:
                return False
