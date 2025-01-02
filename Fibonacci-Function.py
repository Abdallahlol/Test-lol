def fibonacci(n):
  """
  This function calculates the nth Fibonacci number using recursion.

  Args:
    n: The position of the Fibonacci number to calculate (starting from 0).

  Returns:
    The nth Fibonacci number.
  """
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Example usage
n = 10  # Calculate the 10th Fibonacci number
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")