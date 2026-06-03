import heapq
def find_smallest(arr):
    heapq.heapify(arr)
    return heapq.heappop(arr)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_smallest(arr))