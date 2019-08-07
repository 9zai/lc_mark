#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        recs = {}
        curSum = 0

        for i in range(n):
            curSum+=nums[i]
            matches = recs.get(curSum,0)
            
            count+=matches
            if curSum == k:
                count+=1
            requests = recs.get(curSum+k,0)+1

            recs[curSum+k] = requests

        return(count)


    def subarraySumNPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        posSums = [[0 for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(i,n):
                if i == j:
                    posSums[i][j] = nums[i]
                elif i>0:
                    posSums[i][j] = posSums[0][j] - posSums[0][i] + nums[i]
                else:
                    posSums[i][j] = posSums[i][j-1] + nums[j]
                
                if posSums[i][j] == k:
                    count+=1
        
        return(count)
