def sync_add(a, b):
    return a + b

def sync_subtract(a, b):
    return a - b

def sync_multiply(a, b):
    return a * b

def sync_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
