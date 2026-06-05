def max_difference(arr):
    min_element = arr[0]
    max_diff = arr[1]-arr[0]
    for i in range(1, len(arr)):
        diff = arr[i]-min_element
        if diff > max_diff:
            max_diff = diff
        if arr[i]< min_element:
            min_element = arr[i]
    return max_diff
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(max_difference(arr))