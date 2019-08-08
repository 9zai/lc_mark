#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 重新排列日志文件
#
# https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (27.57%)
# Total Accepted:    424
# Total Submissions: 1.5K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# 给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
# 
# 
# 
# 示例：
# 
# 输入：A = [4,5,0,-2,-3,1], K = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 K = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
# 
# 
#
"""
对于连续子数组问题，通常采用前缀和来解决：预处理的方法
即 P[i+1] = sum(A[0],A[i]) --> 那么所有连续子数组和可以表示为 sum[i,j] = P[j] - P[i] j>i
即 改成 求( P[j]-P[i] )整除 K 的个数 --> 转化为 P[j] % K == P[i] % K --> 枚举同余的i,j的个数

难点在于
1. 前缀和代表所有连续子序列和
2. 和整除 到 两个和同余
3. 同余采用 C[count,2] 的枚举计算公式
"""
from collections import Counter
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        n = len(A)
        P = [0 for i in range(n+1)]
        mods = [0 for i in range(n+1)]
       
        for i in range(n):
            P[i+1] = P[i] + A[i]
            mods[i+1] = P[i+1] % K

        counter = Counter(mods) # 自带了字典计数器
        res = 0

        for key in counter:
            value = counter.get(key,0)
            res = res + int((value * (value-1))/2)

        return res

        
        




