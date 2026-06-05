def count_even_odd(arr):
    even = [num for num in arr if num % 2 == 0]
    odd = [num for num in arr if num % 2 != 0]
    return len(even), len(odd)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
even, odd = count_even_odd(arr)
print("Even = ", even)
print("Odd = ", odd)