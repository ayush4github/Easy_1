import heapq
def find_largest(arr):
    heap = []
    for num in arr:
        heapq.heappush(heap, -num)
    return -heapq.heappop(heap)
arr = list(map(int, input("Enter elements of array separated by space :").split()))
print(find_largest(arr))