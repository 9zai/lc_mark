#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
class Solution:
    #O(1) with no swap
    #O(N) -> O(logN) find the swap point

    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            
            if mid == len(nums)-1:
                break

            if nums[mid] > nums[mid+1]:
                return(nums[mid+1])
            
            if nums[mid] < nums[l]:
                r = mid-1
            else:
                l = mid+1

        return(min(nums[0],nums[-1]))
        

