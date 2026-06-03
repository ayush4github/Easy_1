def find_smallest(arr, left, right):
    if left==right:
        return arr[left]
    mid = (left+right)//2
    left_min = find_smallest(arr, left, mid)
    right_min = find_smallest(arr, mid+1, right)
    return min(left_min, right_min)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
left = int(input("Enter start index: "))
right = int(input("Enter length of array: "))-1
print(find_smallest(arr, left, right))