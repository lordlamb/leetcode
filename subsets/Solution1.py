"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
递归解法
"""
from typing import List


class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        else:
            sub = self.subsets(nums[1:])
            ret = []
            for item in sub:
                ret.append(item)
                ret.append([nums[0]] + item)
            return ret

