#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H指数 II
#
class Solution:
    def ON(self, citations:List[int]) -> int:
        #升序啊....XX
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

    def hIndex(self, citations: List[int]) -> int:
        #log means the bi-search until equal or one larger
        n = len(citations)
        l = 0
        r = n-1


        while l<=r:
            mid = (l+r)//2

            if n-mid == citations[mid]:
                return(n-mid)
            elif n-mid > citations[mid]:
                if mid<n-1 and n-(mid+1) < citations[mid+1]:
                    return(n-mid-1)
                else:
                    l = mid+1
            
            if n-mid < citations[mid]:
                r = mid-1
                

        if n == 0:
            return(0)
        return(min(n,citations[0]))


