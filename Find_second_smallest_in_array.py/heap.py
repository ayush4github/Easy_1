import heapq
def find_second_smallest(arr):
    heapq.heapify(arr)
    heapq.heappop(arr)
    return heapq.heappop(arr)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_second_smallest(arr))