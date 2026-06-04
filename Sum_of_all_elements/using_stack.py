def find_sum(arr):
    stack = []
    for num in arr:
        stack.append(num)
    total = 0
    while stack:
        total += stack.pop()
    return total
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_sum(arr))