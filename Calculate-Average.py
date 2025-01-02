def calculate_average(numbers):
  """
  Calculates the average of a list of numbers.

  Args:
    numbers: A list of numbers.

  Returns:
    The average of the numbers in the list.
  """
  if not numbers:
    return 0  # Handle empty list case

  total = sum(numbers)
  average = total / len(numbers)
  return average

# Example usage
my_list = [10, 20, 30, 40, 50]
avg = calculate_average(my_list)
print(f"The average of the numbers is: {avg}") 
