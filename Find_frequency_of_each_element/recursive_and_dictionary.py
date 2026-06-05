def find_frequency(arr, index, freq):
    if index == len(arr):
        return freq
    if arr[index] in freq:
        freq[arr[index]]+=1
    else:
        freq[arr[index]] = 1
    return find_frequency(arr, index+1, freq)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_frequency(arr, 0, {}))