def is_sorted(arr):
    return all(arr[i]<arr[i+1] for i in range(len(arr)-1))
arr = list(map(int, input("Enter eleents of array separated by space: ").split()))
print(is_sorted(arr))