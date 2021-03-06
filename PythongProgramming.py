__author__ = "Jiaqi Li"
import math
import random 
###program1- Rock,paper,scissors
### rock wins against scissor, scissor wins against paper, paper wins against rock
rock = '0'
paper = '1'
scissor = '2'

computer = random.randint(0,3)
user_player = input("It's your turn! Enter 0 for rock, 1 for paper, and 2 for scissor")
#if the user enter a 0, the computer generate three possible outputs (0,1,2), each number corespond to one of the following case
while user_player == "0":
    if computer == 0:
        print("It's a tie, you both have rock")
    elif computer == 1:
        print("The computer wins with paper!")
    elif computer == 2:
        print("You win! Your rock smashes the computer's scissor")
    break
while user_player == "1":
    if computer == 0:
        print("You win!Your paper covers the computer's rock!")
    elif computer == 1 :
        print("It's a tie, you both have paper")
    elif computer == 2 :
        print("You lose! The computer's scissor wins against your paper")
    break
while user_player == '2':
    if computer == 0:
        print("The computer's rock smashes your scissor, you lose...")
    elif computer == 1:
        print("You win!!")
    elif computer == 2:
        print("It's a tie! You both have a scissor")
    break



##
##It's your turn! Enter 0 for rock, 1 for paper, and 2 for scissor0
##You win! Your rock smashes the computer's scissor
##
##    
##It's your turn! Enter 0 for rock, 1 for paper, and 2 for scissor1
##You win!Your paper covers the computer's rock!
##
##It's your turn! Enter 0 for rock, 1 for paper, and 2 for scissor2
##You win!!



#Program2-Coin Change
quarter =25 
dime = 10
nickle = 5
penny = 1
money_value = float(input("Please enter a monetary value"))
money_value = int(money_value*100)

if money_value >= 0:
    num_quarter = money_value // quarter
    #calculate the maximum amount of quarters that can fit into the monetary value the user entered
    remain1 = money_value - num_quarter* quarter
    #calculate how much is left excluding the quarters.
    num_dime = remain1 // dime
    #calculate how many dime is needed
    remain2 = remain1 - num_dime*dime
    #calculate how much money is left after the dimes
    num_nickle = remain2//nickle
    #calculate how many nickles are needed
    remain3 = remain2 - num_nickle*nickle
    #calculate how much money is left after the nickle(s)
    num_penny = remain3//penny
    #calculate how many penny is needed
    remain4 = remain3 - num_penny*penny

    print("Exchanged coins:")
    print("quarters:"+ str(num_quarter))
    print("dime:" + str(num_dime))
    print("nickle:"+ str(num_nickle))
    print("penny:" + str(num_penny))

else:
    print("You enter an invalid value")

#output:
#case1:
##Please enter a monetary value1.54
##Exchanged coins:
##quarters:6
##dime:0
##nickle:0
##penny:4


#case2:
##Please enter a monetary value0
##Exchanged coins:
##quarters:0
##dime:0
##nickle:0
##penny:0

##case3
##Please enter a monetary value-1.5
##You enter an invalid value
    

#program 3 - Marcy's Nested Pizzeria
pizza_per_slice = 1.50
whole = 10
pizza_7 = 10.50
pizza_8 = 10
initial_val = float(input("How much are you paying?"))
payment = 0
to_buy = input("Would you like pizza?").lower()
while to_buy == 'yes' or to_buy == "y":
    amount_pizza = input("Would you like 'slices' or 'whole' pizzas?")
    if amount_pizza == "slices":
        num_slice = int(input("How many slices would you like to buy?"))
        if (num_slice != "7" or num_slice != "seven" )and (num_slice !="8" or num_slice !="eight"):
            #this line of code check if the money the customer has can afford to buy the slices of pizza he/she wants
            if initial_val >= num_slice*pizza_per_slice:
                payment = pizza_per_slice * num_slice
                print("You order: " + str(num_slice) + " slices of pizza")
                print("Your change comes to: " + str(initial_val - payment)+"dollars")
                #if the customer doesn't have enough money, tell them how much more money they need to pay
            else:
                print("The amount of money you give me is not enough, you need " + str(num_slice*pizza_per_slice - initial_val) + " more dollars")
                #when the user is buying 7 slices of pizza, do the following calculation because there is a special price for 7 slices.
        elif num_slice == "7" or num_slice =="seven":
            if initial_val >=pizza_7:
                
                payment = pizza_7
                print("You order: " + str(num_slice) + " slices of pizza")
                print("Your change comes to: " + str(initial_val - payment) + "dollars")
            else:
                print("The amount of money you give me is not enough, you need " + str(pizza_7 - initial_val) + " more dollars")
    elif amount_pizza == "whole":
        if initial_val >=pizza_8:
            payment = pizza_8
            print("You order a whole pizza")
            print("Your change comes to: " + str(initial_val - whole) + "dollars")
        else:
            print("The amount of money you give me is not enough, you need " + str(whole-initial_val) + " more dollars")
    break
else:
    print("order something next time")
        
        
        
##How much are you paying?19
##Would you like pizza?y
##Would you like 'slices' or 'whole' pizzas?slices
##How many slices would you like to buy?7
##You order: 7 slices of pizza
##Your change comes to: 8.5dollars

##How much are you paying?2
##Would you like pizza?y
##Would you like 'slices' or 'whole' pizzas?whole
##The amount of money you give me is not enough, you need 8.0 more dollars

##How much are you paying?34
##Would you like pizza?n
##order something next time

                   
