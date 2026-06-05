def find_duplicates(arr):
    frequency = {}
    duplicates = []
    for num in arr:
        if num in frequency:
            frequency[num] +=1
        else:
            frequency[num] =1
    for num in frequency:
        if frequency[num] > 1:
            duplicates.append(num)
    return duplicates
arr = list(map(int, input("Enter the elements of array separated by space: ").split()))
print(find_duplicates(arr))