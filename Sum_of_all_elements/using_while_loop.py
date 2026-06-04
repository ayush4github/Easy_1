def find_sum(arr):
    total = 0
    index = 0
    while index < len(arr):
        total +=arr[index]
        index +=1
    return total
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_sum(arr))