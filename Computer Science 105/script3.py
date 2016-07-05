#Script 3

keepgoing = 'y'
total = 0
budget = float(input("Enter your budget for this month: "))

while keepgoing == 'y':
    expense = float(input("Enter an expense amount for this month: "))
    total += expense
    output = budget - total
    keepgoing = input("Do you want to enter another expense amount? Type Y for Yes: ")
if budget > total:
    print(" you are over budget by $",output,sep = "")
elif budget == total:
    print("your total expenses is equal to your budget")
else:
    print("You are under budget by $",output*-1,sep= "")
