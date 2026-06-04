def is_sorted(arr, index =0):
    if index == len(arr)-1:
        return True
    if arr[index]> arr[index+1]:
        return False
    return is_sorted(arr, index+1)
arr = list(map(int, input("Enter the elements separated by space: ").split()))
print(is_sorted(arr))