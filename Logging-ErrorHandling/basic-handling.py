try:
    x = 10 / 0  # Will raise ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Handle error
finally:
    print("Execution completed")  # Always runs
