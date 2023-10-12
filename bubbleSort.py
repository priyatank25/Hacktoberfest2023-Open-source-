def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Flag to optimize the algorithm by detecting whether any swaps were made
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps were made in this pass, the list is already sorted
        if not swapped:
            break

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]

print("Unsorted array:", arr)

bubble_sort(arr)

print("Sorted array:", arr)
