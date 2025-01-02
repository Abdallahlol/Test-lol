def factorial(n):
    """
    This function calculates the factorial of a non-negative integer using recursion.

    Args:
        n: The non-negative integer for which to calculate the factorial.

    Returns:
        The factorial of n.
    """
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n-1)  # Recursive case: n! = n * (n-1)! 