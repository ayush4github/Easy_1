def find_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_sum(arr))