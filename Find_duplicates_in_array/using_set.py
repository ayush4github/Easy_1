def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
arr = list(map(int, input("Enter the elements of array separated by space: ").split()))
print(find_duplicates(arr))