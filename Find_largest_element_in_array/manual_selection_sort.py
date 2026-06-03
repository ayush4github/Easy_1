def find_largest(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
                arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr[0]
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_largest(arr))