def myfun3(numbers):
    """This is where i describe what the function does.
    
    Args:
        numbers: Numbers entered by the user.
    
    """

    if (numbers[0] %2 == 0) and (numbers[1] %2 == 0) : # Even
        print(numbers)
        print(min(numbers))
    elif (numbers[0] %2 != 0) and (numbers[1] %2 != 0): # Odd
        print(numbers)
        print(max(numbers))
    else:
        print("I dont like numbers")

number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
numbers = [number1, number2]

myfun3(numbers)
