#Total Odd Number
my_list =[7,13,55,82,17,116,73,91] #List
total = 0

for number in my_list:
    if number % 2 != 0: #Odd Number Check
        total += number

print(f"Total odd numbers:  {total}")



