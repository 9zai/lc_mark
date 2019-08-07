#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        res = []

        queue.insert(0,(0,root))
        res.append([root.val])

        while len(queue) >0:
            (level,expNode) = queue.pop()

            if expNode.left != None:
                if len(res) <= level+1:
                    res.append([expNode.left.val])
                else:
                    res[level+1].append(expNode.left.val)
                queue.insert(0,(level+1,expNode.left))
            
            if expNode.right != None:
                if len(res) <= level+1:
                    res.append([expNode.right.val])
                else:
                    res[level+1].append(expNode.right.val)
                queue.insert(0,(level+1,expNode.right))
        
        for i in range(len(res)):
            if i % 2 == 1:
                res[i].reverse()
        
        return(res)



