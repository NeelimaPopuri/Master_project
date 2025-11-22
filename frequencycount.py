def frequency(arr):
    freq = {}  # hash map

    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    return freq


print(frequency(["a", "b", "a", "c", "a", "b"]))
