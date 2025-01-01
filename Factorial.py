def factorial(n):
    """
    This function calculates the factorial of a given number.

    Args:
      n: The number for which to calculate the factorial.

    Returns:
      The factorial of n.
    """
    if n == 0:
        return 1  # Factorial of 0 is 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = factorial(num)
    print("The factorial of", num, "is", result)
