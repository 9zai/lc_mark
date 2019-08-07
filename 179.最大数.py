#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
import functools
def com(x,y):
        x_str = str(x)
        y_str = str(y)

        if x_str + y_str > y_str + x_str:
            return(-1)
        elif x_str + y_str < y_str + x_str:
            return(1)
        else:
            return(0)

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(nums,key=functools.cmp_to_key(com))
        res = ""

        for i in nums:
            if res == "" and i == 0:
                return("0")
            res = res + str(i)

        return(res)

