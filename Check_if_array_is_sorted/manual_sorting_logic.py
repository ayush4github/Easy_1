def is_sorted(arr):
    temp = arr[:]
    for i in range(len(temp)):
        min_index = i
        for j in range(i+1, len(temp)):
            if temp[j] < temp[min_index]:
                min_index = j
        temp[i], temp[min_index] = temp[min_index], temp[i]
    return arr == temp
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(is_sorted(arr))