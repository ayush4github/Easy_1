def count_even_odd(arr):
    even = 0
    odd = 0
    index = 0
    while index < len(arr):
        if arr[index] % 2 == 0:
            even+=1
        else:
            odd +=1
        index +=1
    return even, odd
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
even, odd = count_even_odd(arr)
print("Even = ", even)
print("Odd = ", odd)