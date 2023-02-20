print ("Hello, I will be helping you calculate the cost of installing fiber optic cable for your company. What is the name of your company?")
company_name=(input())
print ("What is the number of feet of fiber optic to be installed for your company?")
feet_of_cable = input()
feet_of_cable = float(feet_of_cable)
cost_of_cable = feet_of_cable * .97
message = "The cost to insall fiber optic cable for " + str(company_name) + "is " + str(cost_of_cable)
print(message)