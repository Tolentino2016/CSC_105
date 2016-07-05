salary = float(input("Enter salary: "))
years_on_job = float(input("Enter years on the job: "))


if salary >= 30000:
	if years_on_job >= 2:
		print("You qualify")
	else: print("You don't qualify for the loan since you have worked less than two years")
else: print ("You don't qualify because you make less than 30k")