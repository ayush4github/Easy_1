def count_even_odd(arr, index = 0, even = 0, odd= 0):
    if index == len(arr):
        return even, odd
    if arr[index] % 2 == 0:
        even +=1
    else:
        odd +=1
    return count_even_odd(arr, index +1, even, odd)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
even, odd = count_even_odd(arr)
print("Even = ", even)
print("Odd = ", odd)