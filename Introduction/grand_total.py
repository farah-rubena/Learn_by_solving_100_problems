#   Enter the price of a meal at the restaurant. Determine the tax paid for that meal at a tax rate of your choice and tip at the rate of 10% of meal amount without the tax.
#   Display meal price, tax, tip and grand total on different lines in a user friendly format.

price_of_meal = int(input("Enter the price of the meal: "))

tax_rate = int(input("Enter the tax rate: "))

tax_paid = (tax_rate/100) + 1

tip_percent = (10/100) + 1

grand_total = price_of_meal + tax_paid + tip_percent

print(f"Meal Price: {price_of_meal}")
print(f"Tax Rate: {tax_rate}%")
print(f"Tip Percentage: {tip_percent}%")
print(f"Grand Total : {grand_total}")

