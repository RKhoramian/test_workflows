def add_two_numbers(num1, num2):
    return num1 + num2


# Function 2: subtract_two_numbers
def subtract_two_numbers(num1, num2):
    return num1 - num2


# Function 3: multiply_two_numbers
def multiply_two_numbers(num1, num2):
    return num1 * num2


# Function 4: divide_two_numbers
def divide_two_numbers(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Error: division by zero")
