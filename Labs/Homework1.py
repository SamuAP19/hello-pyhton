"""
#First part
annual_salary = int(input("Enter the inicial annual salary"))
total_cost = int(input("Enter a value of your dream house"))
def calc(portion_saved):
    counter = 0
    current_savings = 0
    r = 0.04

    while total_cost*0.25 >= current_savings:
        counter += 1
        current_savings += (annual_salary/12) * portion_saved
        if counter % 12 == 0:
            current_savings *= 1.04

    print(counter)
    return counter

"""
"""
#Second part

annual_salary = int(input("Enter the inicial annual salary"))
total_cost = int(input("Enter a value of your dream house"))
current_savings = 0
r = 0.04
portion_saved = float(input("Enter the amount to be saved per month"))
counter = 0
semi_annual_raise = float(input("Enter in percentage the amount of your raise every 6 months"))

while total_cost*0.25 >= current_savings:
    counter += 1
    current_savings += (annual_salary/12) * portion_saved
    if counter % 6 == 0:
        current_savings += annual_salary * semi_annual_raise
    elif counter % 12 == 0:
        current_savings *= 1.04

print(counter)
print(current_savings)

"""

TOTAL_COST = 1000000.0
SEMI_ANNUAL_RAISE = 0.07
ANNUAL_RETURN = 0.04
PORTION_DOWN_PAYMENT = 0.25
DOWN_PAYMENT_AMOUNT = TOTAL_COST * PORTION_DOWN_PAYMENT
TOTAL_MONTHS = 36
EPSILON = 100.0 


def simulate_savings(start_salary, portion_saved_rate):
    current_savings = 0.0
    current_annual_salary = start_salary
    
    for month in range(1, TOTAL_MONTHS + 1):
        monthly_salary = current_annual_salary / 12
        
        interest = current_savings * (ANNUAL_RETURN / 12)
        current_savings += monthly_salary * portion_saved_rate
        current_savings += interest
        
        if month % 6 == 0:
            current_annual_salary *= (1 + SEMI_ANNUAL_RAISE)
            
    return current_savings

def find_best_rate(starting_salary):
    low = 0.0
    high = 1.0
    steps = 0

    savings_at_100_percent = simulate_savings(starting_salary, 1.0)
    if savings_at_100_percent < DOWN_PAYMENT_AMOUNT:
        print("It is not possible to pay the down payment in three years.")
        return 

    while True:
        steps += 1
        guess_rate = (low + high) / 2.0
        
        final_savings = simulate_savings(starting_salary, guess_rate)
    
        if abs(final_savings - DOWN_PAYMENT_AMOUNT) <= EPSILON:
            break
        
        if final_savings < DOWN_PAYMENT_AMOUNT:
            low = guess_rate
        else:
            high = guess_rate

    print(f"Best savings rate: {guess_rate:.4f}")
    print(f"Steps in bisection search: {steps}")


initial_annual_salary = float(input("Enter the starting salary in Lyon: "))
find_best_rate(initial_annual_salary)



        

