def calculator(option,num1,num2):
    if option == 1:
        result = num1 + num2
        return result
    elif option == 2:
        result = num1 - num2
        return result
    elif option == 3:
        result = num1 * num2
        return result
    elif option == 4:
        if num2 == 0:
            print(f"Error: Division by zero")
            return None
        else:
            result = num1 / num2
            return result
    elif option == 5:
        result = num1 % num2
        return result
    else:
        print("Invalid option")
        return None
  
#Processing Options
print("Option1 = Add")
print("Option2 = Minus")
print("Option3 = Multiplication")
print("Option4 = Division")
print("OPtion5 = Getting Mod")

#Receiving data input from the user
option = int(input("Please select an option: "))
print(f"Your choice of option: {option}")

num1 =float(input("Please select your first number:"))
print(f"Your first number: {num1}")

num2 =float(input("Please select your second number:"))
print(f"Your second number: {num2}")

#Calculation Process
result = calculator(option,num1,num2)
print(f"Your process result: {result}")

if result is not None:
    print(f"Your process result: {result}")