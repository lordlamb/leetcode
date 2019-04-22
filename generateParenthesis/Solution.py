"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
"""

from typing import List;


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        self.generate('', n, 0, 0, ret)
        return ret

    def generate(self, item:str, n: int, left: int, right:int, ret: List[str]):
        if right > left or left > n or right > n:
            return
        if right == n and left == n:
            ret.append(item)
            return

        self.generate(item + '(', n, left + 1, right, ret)
        self.generate(item + ')', n, left, right + 1, ret)
