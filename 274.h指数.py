#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H指数
#
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        
        for i in range(n):
            if (i+1)==citations[n-1-i]:
                return(i+1)
            elif (i+1) > citations[n-1-i]:
                return(i)
        
        if n == 0:
            return(0)
        else:
            return(min(n,citations[0]))

