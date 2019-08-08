#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from collections import deque

class Solution:
    def bruteForce(self, nums:List[int], k:int) -> List[int]:
        #O(kn)
        n = len(nums)
        res = []
        if k == 1:
            return(nums)
        
        window = []
        for i in range(n):
            window.append(nums[i])

            if len(window) == k:
                curMax = window[0]
                for j in range(k):
                    curMax = max(curMax,window[j])
                window.pop(0)
                res.append(curMax)

        return(res)
    def usingDeque(self, nums:List[int], k:int) -> List[int]:
        #O(n), because poping out all the elements that less than nums[i]
        n = len(nums)
        dq = deque()
        res = []
        if k == 1 or n*k == 0:
            return(nums)

        def clearQueue(i):
            if len(dq) == 0:
                return()
            if dq[0] == i-k:
                dq.popleft()
            
            while len(dq) >0:
                if nums[i] <= nums[dq[-1]]:
                    break
                else:
                    dq.pop()


        maxIndex = 0
        curMax = nums[0]
        
        for i in range(k):
            clearQueue(i)
            dq.append(i)
            if nums[i] > curMax:
                curMax = nums[i]
                maxIndex = i
        
        res.append(curMax)

        for i in range(k,n):
            clearQueue(i)
            dq.append(i)
            res.append(nums[dq[0]])
        
        return(res)




    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#        return(self.bruteForce(nums,k))
        return(self.usingDeque(nums,k))
        

