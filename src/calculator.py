def add(a, b):
    return a + b

def subtract(a, b)      # Missing colon - AGENT SHOULD FIX THIS
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b