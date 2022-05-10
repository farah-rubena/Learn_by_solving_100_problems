#   You just open a savings account that earns 2.1 interest per year. Display the amount you will have in your account over 1, 2, 3 years. Initial deposit is 45.
#   Use only 2 decimal places for each amount.

interest_per_year = 2.1
interest = (2.1/ 100) + 1
print(interest)
initial_deposit = 45

first_year = initial_deposit * interest
second_year = first_year * interest
third_year = second_year * interest

print(f"Interest after first year is {first_year:.2f}")
print(f"Interest after 2nd year is {round(second_year,2)}")
print(f"Interest after 3rd year is {round(third_year,2)}")