today = "Saturday" 
today = "Sunday"  # Example value, you can change it as needed

if today == "Sunday" or today == "Saturday":
    print("Today is Sunday")
else:
    print("Today is Saturday")

num1 = input("Enter Your First Number: ")
num2 = input("Enter Your Second Number: ")

make_choice = input("Enter choice : (+,-,/,%,*) ")

if make_choice == "+":
    sum_of_numbers = int(num1) + int(num2)
    print("The sum of two numbers is :", sum_of_numbers)
elif make_choice == "-":
    sub_of_numbers = int(num1) - int(num2)
    print("The subtraction of two numbers is :", sub_of_numbers)
elif make_choice == "/":
    dvd_of_numbers = int(num1) / int(num2)
    print("The division of two numbers is :", dvd_of_numbers)
elif make_choice == "%":
    per_of_numbers = int(num1) % int(num2)
    print("The modulus of two numbers is :", per_of_numbers)
elif make_choice == "*":
    mult_of_numbers = int(num1) * int(num2)
    print("The multiplication of two numbers is :", mult_of_numbers)
else: 
    print("Invalid Choice")