def find_average(arr):
    return sum(arr)/len(arr)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_average(arr))