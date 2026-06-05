def find_frequency(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] +=1
        else:
            freq[num] = 1
    return freq
arr = list(map(int, input("Enter elements of array separated by comma: ").split(",")))
result = find_frequency(arr)
for element in result:
    print(element, " : ", result[element])
#Alternate method to give output
# for element, count in result.items():
#    print(element, " : ", count)