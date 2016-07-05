#script 4
payment =.01
total = 0
days = int(input("Enter number of days would you like to calculate the salary: "))

for x in range(1,days+1):
    payment *= 2
    total += payment
    print ("On day"+str(x)+"the salary is $",payment/2)
print("The total salary is $",total/2)
