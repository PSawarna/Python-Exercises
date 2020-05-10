annual_salary = float(input('Enter your salary: '))
portion_saved = float(input('How much of your salary do you want to save? '))
total_cost = float(input('What does your dream home cost? '))

portion_down_payment = 0.25
rate_of_return = 0.04
monthly_rate_of_return = rate_of_return / 12
monthly_salary = annual_salary / 12
down_payment = total_cost * portion_down_payment
monthly_deposit = monthly_salary * portion_saved
current_savings = 0
months = 0

while current_savings < down_payment:
    months +=1
    current_savings *= 1 + monthly_rate_of_return
    current_savings += monthly_deposit

print('Number of months: ', months)

##with raise
annual_salary = float(input('What is your salary? '))
portion_saved = float(input('How much do you want to save each month? '))
total_cost = float(input('How much does your dream home cost? '))
semi_annual_raise = float(input('What is your semi-annual raise? '))

portion_down_payment = 0.25
rate_of_return = 0.04
monthly_rate_of_return = rate_of_return / 12
monthly_salary = annual_salary / 12
monthly_deposit = monthly_salary * portion_saved
down_payment = total_cost + portion_saved
current_savings = 0
months = 0


while current_savings < down_payment:
	months += 1
	current_savings *= 1 + monthly_rate_of_return
	current_savings += monthly_deposit

	if months % 6 == 0:
		annual_salary * semi_annual_raise
		monthly_deposit

print('Number of months: ', months)
