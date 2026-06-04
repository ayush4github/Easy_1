def reverse_array(arr, left, right):
    if left >=right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse_array(arr, left+1, right-1)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(reverse_array(arr, 0, len(arr)-1))