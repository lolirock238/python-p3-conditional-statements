#!/usr/bin/env python3

def admin_login(username, password):
    """
    Check if username is 'admin' or 'ADMIN' and password is '12345'
    Returns 'Access granted' if valid, otherwise 'Access denied'
    """
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"


def hows_the_weather(temperature):
    """
    Return a weather description based on temperature
    """
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(num):
    """
    Return 'FizzBuzz' for multiples of 15, 'Fizz' for multiples of 3,
    'Buzz' for multiples of 5, or the number itself otherwise
    """
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def calculator(operation, num1, num2):
    """
    Perform basic arithmetic operations (+, -, *, /)
    Returns the result or None for invalid operations
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None