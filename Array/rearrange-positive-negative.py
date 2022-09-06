def rearrange(arr, n):
    print(arr)
    for i in range(1, n):
        key = arr[i]

        if key > 0:
            continue

        j = i - 1
        while j >= 0 and arr[j] > 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print(arr)


arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
n = len(arr)
rearrange(arr, n)
