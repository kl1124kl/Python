__author__ = "Jiaqi Li"
import random
import tkinter as tk
class Dice:

    def __init__(self):
        self.__value = 1
        self.__img_one = tk.PhotoImage(file='die_face_1_T.png')
        self.__img_two = tk.PhotoImage(file='die_face_2_T.png')
        self.__img_three = tk.PhotoImage(file='die_face_3_T.png')
        self.__img_four = tk.PhotoImage(file='die_face_4_T.png')
        self.__img_five = tk.PhotoImage(file='die_face_5_T.png')
        self.__img_six = tk.PhotoImage(file='die_face_6_T.png')


    def get_image(self):
        if self.__value==1:
            return self.__img_one
        elif self.__value==2:
            return self.__img_two
        elif self.__value==3:
            return self.__img_three
        elif self.__value==4:
            return self.__img_four
        elif self.__value==5:
            return self.__img_five
        else:
            return self.__img_six

        
    def roll(self):
        self.__value = random.randint(1,6)


class MyGUI():

    def __init__(self):
        self.main_window = tk.Tk()
        self.top_frame = tk.Frame(self.main_window)
        #This is dice 1
        self.my_dice1 = Dice()
        self.my_dice1_label = tk.Label(self.top_frame,image = self.my_dice1.get_image())
        self.my_dice1_label.pack(side = tk.LEFT)

        #This is dice2
        self.my_dice2 = Dice()
        self.my_dice2_label = tk.Label(self.top_frame,image = self.my_dice2.get_image())
        self.my_dice2_label.pack(side = tk.LEFT)

        #This is dice3
        self.my_dice3 = Dice()
        self.my_dice3_label = tk.Label(self.top_frame,image = self.my_dice3.get_image())
        self.my_dice3_label.pack(side = tk.LEFT)
        #checkbutton1
        self.dice1_var = tk.IntVar()
        self.dice1_var.set(0)
        self.dice1_cb = tk.Checkbutton(self.top_frame)
        self.dice1_cb.pack(side = tk.LEFT)
        

        button = tk.Button(self.main_window, 
                   text= "roll", 
                   fg="red",command = self.button_press)

        
        button.pack()

        self.top_frame.pack()
        main_window.mainloop()
        
    def button_press(self):
        if self.dice1_var.get() == 1:
            self.my_dice1.roll()
            self.my_dice1_label.config(image = self.my_dice1.get_image())
            
        self.my_dice2.roll()
        self.my_dice2_label.config(image = self.my_dice2.get_image())
        self.my_dice3.roll()
        self.my_dice3_label.config(image = self.my_dice3.get_image())
        
        
##my_dice = Dice()
##print(my_dice.get_value)
##my_dice.roll()
##print(my_dice.get_value())

my_object = MyGUI()
