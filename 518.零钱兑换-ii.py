#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
# https://leetcode-cn.com/problems/coin-change-2/description/
#
# algorithms
# Medium (39.62%)
# Total Accepted:    812
# Total Submissions: 2.1K
# Testcase Example:  '5\n[1,2,5]'
#
# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
# 
# 
# 
# 
# 
# 
# 示例 1:
# 
# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 
# 示例 2:
# 
# 输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
# 
# 
# 示例 3:
# 
# 输入: amount = 10, coins = [10] 
# 输出: 1
# 
# 
# 
# 
# 注意:
# 
# 你可以假设：
# 
# 
# 0 <= amount (总金额) <= 5000
# 1 <= coin (硬币面额) <= 5000
# 硬币种类不超过 500 种
# 结果符合 32 位符号整数
# 
# 
#
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)+1
        dp = [[0 for i in range(amount+1)] for j in range(m)]
        '''
        递推公式的边界 & 循环的逻辑
        i代表使用了ith coins
        j代表amount
        所以 base = dp[i-1][j] --没有ith时的数量
        dp[i][j] = base + dp[i-1][j - coins[i-1]]
        可后续优化为一维数组

        边界条件，所有amount = 0 时有1解，没有硬币时对 0 有一解
        边界 + 1 因为对应 0 amount & [] coins
        '''
        dp[0][0] = 1

        for i in range(1,m):#loop to using ith coins
            dp[i][0] = 1
            for j in range(1,amount+1):
                dp[i][j] = dp[i-1][j]
                if  j - coins[i-1]>=0:
                    dp[i][j] = dp[i][j] + dp[i][j - coins[i-1]]
        
        return(dp[len(coins)][amount])



        

