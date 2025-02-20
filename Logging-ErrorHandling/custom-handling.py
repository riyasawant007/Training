class CustomError(Exception):
    pass

def check_value(x):
    if x < 0:
        raise CustomError("Value cannot be negative")

try:
    check_value(-5)
except CustomError as e:
    print(f"Custom Error: {e}")
