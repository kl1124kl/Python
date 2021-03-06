__author__ = "Jiaqi Li"
user_tax_plan = input("Please enter your tax plan")
user_income = int(input("Please enter your income."))
flat_plan_rate = 0.18
pro_tax_rate1 = 0.03
pro_tax_rate2 = 0.12
pro_tax_rate3 = 0.22
pro_tax_rate4 = 0.39
pro_tax_rate5 = 0.63

regre_tax_rate1 = 0.45
regre_tax_rate2 = 0.28
regre_tax_rate3 = 0.17
regre_tax_rate4 = 0.1                 
#flat tax plan
if user_tax_plan == "F" or user_tax_plan =="f":
    take_home_pay = user_income - user_income * flat_plan_rate
    print("Your income is " + str(user_income))
    print("Base on a /'" + user_tax_plan +" plan,")
    print("Your income will be taxed at a rate of " + str(flat_plan_rate)+ "percent.")
    print("Your take home payment is " + str(take_home_pay))


#progressive tax
elif (user_tax_plan == "B" or user_tax_plan =="f"):
    if user_income < 30000:
        take_home_pay = user_income - user_income * pro_tax_rate1
        print("Your income is " + str(user_income))
        print("Base on a /'" + user_tax_plan +",")
        print("Your income will be taxed at a rate of " + str(pro_tax_rate1)+ "percent.")
        print("Your take home payment is " + str(take_home_pay))
    elif (user_income > 300000 and user_income < 80000):
        take_home_pay = user_income - user_income * pro_tax_rate2
        print("Your income is " + str(user_income))
        print("Base on a /'" + user_tax_plan +"/',")
        print("Your income will be taxed at a rate of " + str(pro_tax_rate2)+ "percent.")
        print("Your take home payment is " + str(take_home_pay))
    elif (user_income > 80000 and user_income < 200000):
        take_home_pay = user_income - user_income * pro_tax_rate3
        print("Your income is " + str(user_income))
        print("Base on a /'" + user_tax_plan +"/',")
        print("Your income will be taxed at a rate of " + str(pro_tax_rate3)+ "percent.")
        print("Your take home payment is " + str(take_home_pay))
    elif (user_income > 200000 and user_income < 1000000):
        take_home_pay = user_income - user_income * pro_tax_rate4
        print("Your income is " + str(user_income))
        print("Base on a /'" + user_tax_plan +"/',")
        print("Your income will be taxed at a rate of " + str(pro_tax_rate4)+ "percent.")
        print("Your take home payment is " + str(take_home_pay))
    else:
        take_home_pay = user_income - user_income * pro_tax_rate5
        print("Your income is " + str(user_income))
        print("Base on a /'" + user_tax_plan +"/',")
        print("Your income will be taxed at a rate of " + str(pro_tax_rate5)+ "percent.")
        print("Your take home payment is " + str(take_home_pay))
#equation
elif (user_tax_plan == "E" or user_tax_plan == "e"):
    if(user_income == 100000):
        take_home_pay = user_income - user_income * 0.0866
        print("Your income is " + str(user_income))
        print("Your income will be taxed at a rate of " + str(pro_tax_rate4)+ "percent.")
        print("Your take home payment is " + str(take_home_pay))
   
#regressive
elif (user_tax_plan == "R" or user_tax_plan == "r"):
    if(user_income < 60000):
        take_home_pay = user_income - user_income * regre_tax_rate1
        print("Your income is " + str(user_income))
        print("Your income will be taxed at a rate of " + str(regre_tax_rate1)+ "percent.")
        print("Your take home payment is " + str(take_home_pay))
    elif (user_income < 120000 and user_income>60000):
        take_home_pay = user_income - user_income * regre_tax_rate2
        print("Your income is " + str(user_income))
        print("Your income will be taxed at a rate of " + str(regre_tax_rate2)+ "percent.")
        print("Your take home payment is " + str(take_home_pay))
    elif(user_income < 2000000 and user_income>120000):
        take_home_pay = user_income - user_income * regre_tax_rate3
        print("Your income is " + str(user_income))
        print("Your income will be taxed at a rate of " + str(regre_tax_rate3)+ "percent.")
        print("Your take home payment is " + str(take_home_pay))
    elif(user_income > 10000000):
        take_home_pay = user_income - user_income * regre_tax_rate4
        print("Your income is " + str(user_income))
        print("Your income will be taxed at a rate of " + str(regre_tax_rate4)+ "percent.")
        print("Your take home payment is " + str(take_home_pay))
else:
    print("Not a valid tax plan")                          


