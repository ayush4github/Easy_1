def find_frequency(arr):
    arr.sort()
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            count +=1
        else:
            print (arr[i-1], " -> ", count)
            count = 1
    print (arr[-1], " -> ", count)
arr = list(map(int, input("Ënter elements of array separated by space: ").split()))
find_frequency(arr)