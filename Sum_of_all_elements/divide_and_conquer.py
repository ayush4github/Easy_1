def find_sum(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left+right)//2
    left_sum = find_sum(arr, left, mid)
    right_sum = find_sum(arr, mid+1, right)
    return left_sum + right_sum
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_sum(arr, 0, len(arr)-1))