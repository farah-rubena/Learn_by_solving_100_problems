# Determine the sum of digits for a 3 digits number. The program should display the following format for exemple 254: 2+5+4=11

#Solution 1

num_to_be_summed = input("Enter the number to be summed: ")
summed_num = 0

for num in num_to_be_summed:

    summed_num += int(num)

print(f"{num_to_be_summed} : {num_to_be_summed[0]} + {num_to_be_summed[1]} + {num_to_be_summed[2]} = {summed_num}")


#OR Solution 2

num_to_be_sum = int(input("Enter the number to be summed: "))
last_num = num_to_be_sum % 10
first_num = num_to_be_sum // 100
second_num = num_to_be_sum // 10%10
sum_all_digits = first_num + second_num + last_num
print(f"{num_to_be_sum} : {first_num} + {second_num} + {last_num} = {sum_all_digits}")
