# ask the hourly rate of the user
hourly_rate = raw_input("What is your hourly rate?")

# convert hourly rate to float 
hourly_rate = float(hourly_rate)

# ask the number of hours that the user has worked
hours_worked = raw_input("How many hours did you work?")

# convert hours worked to float
hours_worked = float(hours_worked)

# multiply the hourly rate and the number of hours worked
gross_income = hourly_rate * hours_worked

# get the 10% of the gross income
deduction = gross_income * .10

# add 1 to the deduction
total_deductions = deduction + 1

# subtract the deductions to the gross income
net_income = gross_income - total_deductions

# show the gross income, net income and deductions to the user
print "Gross Income: " + str(gross_income)
print "Net Income: " + str(net_income)
print "Total Deductions: " + str(total_deductions)