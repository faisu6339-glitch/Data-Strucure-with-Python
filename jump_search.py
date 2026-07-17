import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while prev < n and arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while prev < min(step, n):
        if arr[prev] == target:
            return prev
        prev += 1
    return -1

arr = [2,5,8,12,16,23,38,56,72,91]
target = 23
idx = jump_search(arr,target)
if idx != -1:
    print(f"Element {target} found at index {idx}")
else:
    print("Element not found")
