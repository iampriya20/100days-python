def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

arr = list(map(int, input("Enter a sorted list (e.g., 1 3 4 7 9): ").split()))
target = int(input("Enter target: "))
idx = binary_search(arr, target)
print(idx)
