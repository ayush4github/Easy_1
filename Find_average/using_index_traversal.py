def find_average(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total / len(arr)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_average(arr))