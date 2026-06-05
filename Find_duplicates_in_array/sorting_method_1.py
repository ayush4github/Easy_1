def find_duplicates(arr):
    duplicates = set()
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            duplicates.add(arr[i])
    return duplicates
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_duplicates(arr))