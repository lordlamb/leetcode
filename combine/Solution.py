"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
"""
from typing import List


class Solution:
    """
    使用组合的公式：C(n, k) = C(n-1, k) + C(n-1, k - 1)
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return [[]]
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        elif k == n:
            return [[i for i in range(1, n + 1)]]
        else:
            ret = self.combine(n - 1, k)
            for item in self.combine(n - 1, k - 1):
                ret.append(item + [n])
            return ret


