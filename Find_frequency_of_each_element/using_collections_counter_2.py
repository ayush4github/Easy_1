from collections import Counter
def find_frequency(arr):
    frequency = Counter(arr)
    result = []
    for element, count in frequency.items():
        result.append(f"{element} : {count}")
    return result
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(find_frequency(arr))