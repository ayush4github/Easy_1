def count_even_odd(arr):
    even = 0
    odd = 0
    for num in arr: 
        if num % 2 == 0:
            even += 1
        if num % 2 != 0:
            odd +=1
    return even, odd
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
even, odd = count_even_odd(arr)
print("Even = ", even)
print("Odd = ", odd)