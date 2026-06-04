def find_average(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left+right)//2
    left_sum = find_average(arr, left, mid)
    right_sum = find_average(arr, mid+1, right)
    if left == 0 and right == len(arr)-1:
        return (left_sum + right_sum ) / len(arr)
    return left_sum + right_sum
arr = list(map(int, input("Enter elements of array separated by spaace: ").split()))
print(find_average(arr, 0, len(arr)-1))