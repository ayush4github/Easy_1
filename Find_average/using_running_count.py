def find_average(arr):
    total = 0
    count = 0
    for num in arr:
        total +=num
        count +=1
    return total / count
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_average(arr))