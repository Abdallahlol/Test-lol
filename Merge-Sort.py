def merge_sort(arr):
    """
    Sorts an array in ascending order using the merge sort algorithm.

    Args:
        arr: The array to be sorted.

    Returns:
        The sorted array.
    """
    if len(arr) <= 1:
        return arr  # Base case: array with 0 or 1 element is already sorted

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)  # Recursively sort the left half
    right_half = merge_sort(right_half)  # Recursively sort the right half

    return merge(left_half, right_half)

def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.

    Args:
        left: The first sorted array.
        right: The second sorted array.

    Returns:
        A new sorted array containing elements from both input arrays.
    """
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])  # Append any remaining elements from the left array
    merged.extend(right[j:])  # Append any remaining elements from the right array

    return merged

# Example usage
unsorted_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = merge_sort(unsorted_array)
print("Sorted array:", sorted_array)