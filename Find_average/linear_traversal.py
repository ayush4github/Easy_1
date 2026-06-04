def find_average(arr):
    total = 0
    for num in arr:
        total +=num
    return total / len(arr)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_average(arr))