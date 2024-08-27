def bucketSort(arr):
    # Assuming arr only contains 0, 1 or 2 (I see...the values can't be dynamically defined)
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1

    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)): # This n assignment would only work for the case of 0, 1, 2...
        for j in range(counts[n]): # This inner loop is just repeating the assignment of the bucket
            arr[i] = n
            i += 1
    return arr