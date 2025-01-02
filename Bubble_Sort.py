def bubble_sort(arr):
  """
  Sorts an array in ascending order using the bubble sort algorithm.

  Args:
    arr: The array to be sorted.

  Returns:
    The sorted array.
  """
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j] 
  return arr

# Example usage
unsorted_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(unsorted_array)
print("Sorted array:", sorted_array)