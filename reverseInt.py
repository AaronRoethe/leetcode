x = 1234

def reverse(x: int) -> int:
    """
    Take the input value and remove the sign adding it back last. 
    While there's a reminder in x, each iterations removes the last digit
    through integer division `//= 10`
    the first iteration will start with 0 + abs(x) % 10 which will retrive the 
    last digit. By doing both things you can retrieve the the digit and remove 
    from remained, on the next iter you increase the base by 10 and add the new.
    Eventual you'll be left with a x_remaining <= 10 which will result in 0 
    that will close the loop.
    Finally you add the sign back if was original a negative before return.
    """
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        # 4 = 0 + 4
        x_remaining //= 10
        # 123

    return -result if x < 0 else result

print(x)
print(reverse(x))