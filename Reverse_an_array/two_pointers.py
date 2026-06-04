def reverse_array(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1
    return arr
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(reverse_array(arr))