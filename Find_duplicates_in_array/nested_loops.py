def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                if arr[i] not in duplicates:
                    duplicates.append(arr[i])
    return duplicates
arr = list(map(int, input("Ënter the elements of array separated by space: ").split()))
print(find_duplicates(arr))