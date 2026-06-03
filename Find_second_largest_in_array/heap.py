import heapq
def find_second_largest(arr):
    heap = []
    for num in arr:
        heapq.heappush(heap, -num)
    heapq.heappop(heap)
    return -heapq.heappop(heap)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_second_largest(arr))