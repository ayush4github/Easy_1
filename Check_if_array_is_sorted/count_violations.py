def is_sorted(arr):
    count = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            count +=1
    return count == 0
arr = list(map(int, input("Enter the elements of array separated by space: ").split()))
print(is_sorted(arr))