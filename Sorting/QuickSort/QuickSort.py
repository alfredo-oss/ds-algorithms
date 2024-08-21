def quickSort(arr: list[int], s: int, e: int) -> list[int]:
    if e - s + 1 <= 1:
        return arr
    
    pivot = arr[e]
    left = s # pointer for the left side (which allows us to insert the values in the corresponding order)

    # Partition: elements smaller than pivot on the left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left] # we save the element that the left pointer is at because it will be swapped
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1
    
    # Move pivot in between left and right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # Quick sort the left side
    quickSort(arr, s, left - 1)

    # Quick sort the right side
    quickSort(arr, left + 1, e)

    return arr

