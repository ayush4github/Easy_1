def find_largest(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left+right)//2
    left_max = find_largest(arr, left, mid)
    right_max = find_largest(arr, mid+1, right)
    return max(left_max, right_max)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
left = int(input("Enter starting index: "))
right = int(input("Enter number of elements in array : "))-1
print(find_largest(arr, left, right))