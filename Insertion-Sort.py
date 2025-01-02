def insertion_sort(arr):
    """
    Sorts an array in ascending order using the insertion sort algorithm.

    Args:
        arr: The array to be sorted.

    Returns:
        The sorted array.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
unsorted_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = insertion_sort(unsorted_array)
print("Sorted array:", sorted_array)