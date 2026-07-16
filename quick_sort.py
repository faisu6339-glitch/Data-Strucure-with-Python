def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    data = [34, 7, 23, 32, 5, 62]
    print("Original array:", data)
    sorted_data = quick_sort(data)
    print("Sorted array:  ", sorted_data)
