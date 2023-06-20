
def add_num(num1,num2):
    return num1 + num2

def minus_num(num1,num2):
    return  num1 - num2

def multiply_numbers(num1,num2):
    return num1 * num2

def divide_numbers(num1,num2):
    return num1 / num2

while True: 
    print("Choose your option below: \n")
    print("A. Addition")
    print("B. subtraction")
    print("C. multiplication")
    print("D. division")
    print("E. exit")

    user_choice = input('Enter your choice:')

    if user_choice.upper() == "A":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter your second number: "))
        print(add_num(num1, num2))
    elif user_choice.upper() =="B":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter your second number: "))
        print(minus_num(num1, num2))
    elif user_choice.upper() =="C":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter your second number: "))
        print(multiply_numbers(num1, num2))
    elif user_choice.upper()=="D":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter your second number: "))
        print(divide_numbers(num1, num2))
    elif user_choice.upper() =="E":
        print("program ended")
        quit()
    else:
        print("the option does not exist please try again")