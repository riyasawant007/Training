try:
    x = int("abc")  # Will raise ValueError
except (ValueError, TypeError) as e:
    print(f"Handled Error: {e}")
