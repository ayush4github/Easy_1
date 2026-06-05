def find_frequency(arr):
    visited = []
    for i in range(len(arr)):
        if arr[i] in visited:
            continue
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count +=1
        print(arr[i], " -> ", count)
        visited.append(arr[i])
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
find_frequency(arr)