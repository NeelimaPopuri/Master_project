from typing import List


class Solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i


# create object
s = Solution()
print(s.twosum([2, 7, 11, 15], 9))
