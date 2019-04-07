"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
非递归解法
"""
from typing import List


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for i in nums:
            for item in ret[:]:
                ret.append([i] + item)

        return ret

