def two_sum(nums, target):
    mp = {}  # hash map (value -> index)

    for i, n in enumerate(nums):
        diff = target - n
        if diff in mp:
            return [mp[diff], i]
        mp[n] = i


print(two_sum([2, 7, 11, 15], 9))
