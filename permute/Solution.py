"""
给定一个没有重复数字的序列，返回其所有可能的全排列。
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            ret = []
            for i in range(len(nums)):
                sub_permute = self.permute(nums[0:i] + nums[i + 1:len(nums)])

                for item in sub_permute:
                    ret.append([nums[i]] + item)

            return ret

