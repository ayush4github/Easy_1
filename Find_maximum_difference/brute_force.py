def max_difference(arr):
    max_diff = arr[1]-arr[0]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            diff = arr[j]-arr[i]
            if diff > max_diff:
                max_diff = diff
    return max_diff
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(max_difference(arr))