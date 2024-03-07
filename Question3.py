"""Value Error"""
def validate_range(min_val, max_val):
    """range check"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not min_val <= arg <= max_val:
                    raise ValueError(f"Argument '{arg}' is not in the range [{min_val}, {max_val}]")
            return func(*args, **kwargs)
        return wrapper
    return decorator
@validate_range(1, 10)
def generate_square_of_even_numbers():
    """even number check"""
    return [x**2 for x in range(1, 11) if x % 2 == 0]
try:
    result = generate_square_of_even_numbers()
    print(result)
except ValueError as e:
    print(e)
