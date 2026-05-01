
def add(a, b):
    try:
        return a + b
    except TypeError as e:
        print(f"Error: {e}")

def subtract(a, b):
    try:
        return a - b
    except TypeError as e:
        print(f"Error: {e}")

def multiply(a, b):
    try:
        return a * b
    except TypeError as e:
        print(f"Error: {e}")

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")