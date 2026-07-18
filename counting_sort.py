def counting_sort(arr):
    if not arr:
        return arr
    if min(arr) < 0:
        raise ValueError("This implementation supports non-negative integers only.")
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    i = 0
    for value, freq in enumerate(count):
        while freq > 0:
            arr[i] = value
            i += 1
            freq -= 1
    return arr

if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]
    print("Original Array:", arr)
    counting_sort(arr)
    print("Sorted Array:", arr)
