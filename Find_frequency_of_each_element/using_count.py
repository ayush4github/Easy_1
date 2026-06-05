def find_frequency(arr):
    visited = []
    for num in arr:
        if num not in visited:
            print(num , " -> ", arr.count(num))
            visited.append(num)
arr = list(map(int, input("Enter the elements of array separated by space: ").split()))
find_frequency(arr)