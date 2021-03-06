##Author: Jiaqi Li
##Date: 12/2018
import tkinter as tk
import tkinter.messagebox
import random
class Item:
    def __init__(self):
        self.__price = 10.0
        self.__quantity = 15
        self.__name = "Eyeshadow"
        self.__image = tk.PhotoImage(file = self.__name+'.png' ).subsample(4)
        self.__total_before = 0
        self.__total_after = 0
    def set_price(self,p):
        self.__price = p
    def set_quantity(self,q):
        self.__quantity = q
    def set_nameImage(self,n):
        #the image name and the product name are the same
        self.__name = n
        self.__image = tk.PhotoImage(file = self.__name+'.png' ).subsample(4)
    def get_price(self):
        return self.__price
    def get_name(self):
        return self.__name
    def get_image(self):
        return self.__image
    def get_quantity(self):
        return self.__quantity


    
class Inventory:
    def __init__(self):
        #create a dictoinary
        self.__inventory = {}
        
        file = open("myInventory.txt","r")
        #read from the file, each line of the file represent the name, price, and the quantity of the item, use the setters to set items' name,quantity,and prices
       
        line=file.readline()
        while line!='':
            item = Item()
            item.set_nameImage(line[:-1])#get rid of the newline at the end
            item.set_price(float(file.readline()[:-1]))
            item.set_quantity(int(file.readline()))
            self.__inventory[item.get_name()] = item
            

            line=file.readline()

        file.close()

    def get_image(self,key):
        return self.__inventory[key].get_image()
    def get_price(self,key):
        return self.__inventory[key].get_price()
    #This method checks if the desired purchased amount is less than the quantity in stock
    def get_item(self,key,n):
        if self.__inventory[key].get_quantity() >= n:
            self.__inventory[key].set_quantity(self.__inventory[key].get_quantity() - n)
            item = Item()
            item = self.__inventory[key]
            item.set_quantity(n)
            return item
        else:
            #If user enter a quantity matches the quantity of the product in stock, set the product's quantity to 0
            n=self.__inventory[key].get_quantity()
            self.__inventory[key].set_quantity(0)
            item = Item()
            item = self.__inventory[key]
            item.set_quantity(n)
            return item
        
class ShoppingCart:
    def __init__(self):
        self.__shoppingCart = {}
    def add_item(self,item):
        #add all the chosen items to the shopping cart, each item is an object
        self.__shoppingCart[item.get_name()] = item
    #This method calculates the sub total
    def get_total(self):
        total = 0
        for key in self.__shoppingCart:
            total += self.__shoppingCart[key].get_price() * self.__shoppingCart[key].get_quantity()
        total = self.cost_after_discount(total)
        return total
    def get_shoppingCart(self):
        return self.__shoppingCart
    # user gets discount if the sub total is within the following domain
    def cost_after_discount(self,total_before):
        if total_before >=40 and total_before < 80:
            return total_before - 5
        elif total_before >=80 and total_before < 120:
            return total_before - 10
        elif total_before >120:
            return total_before - 20
        else:
            return total_before
    

class MyGUI:
    def __init__(self):
        #create the main window
        self.main_window = tk.Tk()
    
        self.myInventory = Inventory()
        self.shoppingCart = ShoppingCart()
        
        #create the top frame, there are three buttons representing three different items inside the top frame,

        self.right_frame = tk.Frame(self.main_window)
        #first item
        self.pic1label = tk.Label(self.right_frame,image = self.myInventory.get_image('Eyeshadow'))

        self.pic1label.pack(side = tk.TOP)
        
        self.qty_label1 = tk.Label(self.right_frame, text = 'Qty: ')
        self.qty_label1.pack(side = tk.TOP)
        
        self.label2 = tk.Label(self.right_frame)
        self.CB1 = tk.IntVar()
        #By default, the variable is set to 1 if the button is selected, and 0 otherwise.
        self.CB1.set(0)
        self.checkButton = tk.Checkbutton(self.label2, variable=self.CB1)
        self.checkButton.pack(side = tk.LEFT)
        self.qty_entry = tk.Entry(self.label2,width = 6)
        self.qty_entry.pack(side = tk.LEFT)
        self.label2.pack(side = tk.TOP)

        self.right_frame.pack(side = tk.LEFT)
        #second item
        self.middle_frame = tk.Frame(self.main_window)
        self.pic2label = tk.Label(self.middle_frame,image = self.myInventory.get_image('Lipstick'))
        self.pic2label.pack(side = tk.TOP)
        
        self.LSqty_label = tk.Label(self.middle_frame, text = 'Qty: ')
        self.LSqty_label.pack(side = tk.TOP)
        
        self.label3 = tk.Label(self.middle_frame)
        self.LipStickCB = tk.IntVar()
        #By default, the variable is set to 1 if the button is selected, and 0 otherwise.
        self.LipStickCB.set(0)
        self.LScheckButton = tk.Checkbutton(self.label3, variable = self.LipStickCB)
        self.LScheckButton.pack(side = tk.LEFT)
        self.LSqty_entry = tk.Entry(self.label3,width = 6)
        self.LSqty_entry.pack(side = tk.LEFT)
        self.label3.pack(side = tk.TOP)
        
        self.middle_frame.pack(side = tk.LEFT)

        #third item
        self.right_frame = tk.Frame(self.main_window)
        self.pic3label = tk.Label(self.right_frame,image = self.myInventory.get_image('Perfume'))
        self.pic3label.pack(side = tk.TOP)
        
        self.LSqty_label = tk.Label(self.right_frame, text = 'Qty: ')
        self.LSqty_label.pack(side = tk.TOP)
        
        self.label4 = tk.Label(self.right_frame)
        self.PerfumeCB = tk.IntVar()
        #By default, the variable is set to 1 if the button is selected, and 0 otherwise.
        self.PerfumeCB.set(0)
        self.PcheckButton = tk.Checkbutton(self.label4, variable = self.PerfumeCB)
        self.PcheckButton.pack(side = tk.LEFT)
        self.Pqty_entry = tk.Entry(self.label4,width = 6)
        self.Pqty_entry.pack(side = tk.LEFT)
        self.label4.pack(side = tk.TOP)
        self.right_frame.pack(side = tk.LEFT)

        self.bottom_frame = tk.Frame(self.main_window)
        self.checkOutButton = tk.Button(self.main_window,text = " check out ",command = self.button1_press)
        self.checkOutButton.pack(side = tk.TOP)
        self.bottom_frame.pack(side = tk.TOP)

        self.main_window.mainloop()
    def button1_press(self):
      
        self.sub_mainwindow = tk.Toplevel()
        
        self.sale_history_file = open('sales_history.txt','w')
        #If the checkbox is checked
        if self.CB1.get()==1:
          
            user_qty = int(self.qty_entry.get())
          
            self.sale_history_file.write(str(user_qty))
            #add this item to the shopping cart
            self.shoppingCart.add_item(self.myInventory.get_item('Eyeshadow',user_qty))
        
        if self.LipStickCB.get()==1:
 
            LSuser_qty = int(self.LSqty_entry.get())
      
            self.sale_history_file.write(str(LSuser_qty))
            self.shoppingCart.add_item(self.myInventory.get_item('Lipstick',LSuser_qty))
        if self.PerfumeCB.get()==1:
            Perfume_entry = int(self.Pqty_entry.get())
           
            self.sale_history_file.write(str(Perfume_entry))
            self.shoppingCart.add_item(self.myInventory.get_item('Perfume',Perfume_entry))
        #print(type(self.shoppingCart))
      
        #Write the items in the shopping cart to a file
        for item in self.shoppingCart.get_shoppingCart():
            print(item)
            self.sale_history_file.write(item)
            
        self.sale_history_file.close()

##        keylist = self.shoppingCart.get_shoppingCart().keys()
##        keylist.sort()
##        
        #shows the user the sub total of the purchase
        tkinter.messagebox.showinfo('order summary',str(self.shoppingCart.get_total()) + ' dollars is your total')

        user_answer = int(input("Thank you for shopping with us! Enter a number from 1 to 5 to win a coupon for future purchase!"))
        
        ranNum = random.randint(1,5)
        if ranNum == user_answer:
            print("Congrats! You just won a 20% coupon! Have a nice day!")
        else:
            print("Better luck next time!")

        self.sub_mainwindow.mainloop()
        

my_obj = MyGUI()



