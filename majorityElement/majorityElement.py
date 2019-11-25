"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ret = 0
        count = 0
        for num in nums:
            if count == 0:
                ret = num
                count = 1
            elif num == ret:
                count += 1
            else:
                count -= 1

        return ret
    