def find_duplicates(arr, index=0, seen = None, duplicates = None):
    if seen is None:
        seen = set()
    if duplicates is None:
        duplicates = set()
    if index == len(arr):
        return list(duplicates)
    if arr[index] in seen:
        duplicates.add(arr[index])
    else:
        seen.add(arr[index])
    return find_duplicates(arr, index+1, seen, duplicates)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_duplicates(arr))