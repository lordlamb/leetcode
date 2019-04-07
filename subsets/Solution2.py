"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
位运算
"""
from typing import List

class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_length = len(nums)
        ret = []
        for i in range(2 ** nums_length):
            print(i)
            item = []
            for j in range(nums_length):
                if (1 << j) & i:
                    item = item + [nums[j]]
            ret.append(item)

        return ret

