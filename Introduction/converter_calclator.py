#   Write a program that converts days in seconds, Celsius in Fahrenheit, miles in centimeters.

days = int(input("Enter the number of days: "))
celcius = float(input("Enter temperature in celcius: "))
miles = int(input("Enter distance in miles: "))

days_in_seconds = days + 3600
celcius_to_fahrenheit = (celcius + 9/5) + 32
miles_to_centimeters = miles * 160934

print(f"Days in seconds: {days_in_seconds}")
print(f"Celcius in Fahrenheit: {celcius_to_fahrenheit}")
print(f"Miles in centimeters: {miles_to_centimeters}")