def helper(arr, index, min_element, max_diff):
    if index == len(arr):
        return max_diff
    max_diff = max(max_diff, arr[index]-min_element)
    min_element = min(min_element, arr[index])
    return helper(arr, index +1, min_element, max_diff)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(helper(arr, 1, arr[0], arr[1]-arr[0]))