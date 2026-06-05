def remove_duplicates(arr):
    if len(arr) == 0:
        return []
    unique_index = 0
    for current_index in range(1, len(arr)):
        if arr[current_index] != arr[unique_index]