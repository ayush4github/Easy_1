def reverse_array(arr):
    stack = []
    for num in arr:
        stack.append(num)
    result = []
    while stack:
        result.append(stack.pop())
    return result
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(reverse_array(arr))