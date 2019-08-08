#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
# https://leetcode-cn.com/problems/course-schedule/description/
#
# algorithms
# Medium (43.41%)
# Total Accepted:    2.6K
# Total Submissions: 5.9K
# Testcase Example:  '2\n[[1,0]]'
#
# 现在你总共有 n 门课需要选，记为 0 到 n-1。
# 
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
# 
# 给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？
# 
# 示例 1:
# 
# 输入: 2, [[1,0]] 
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
# 
# 示例 2:
# 
# 输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
# 
# 说明:
# 
# 
# 输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
# 你可以假定输入的先决条件中没有重复的边。
# 
# 
# 提示:
# 
# 
# 这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
# 通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
# 
# 拓扑排序也可以通过 BFS 完成。
# 
# 
# 
#
"""
拓扑排序：用于DAG，用于描述人物之间依赖关系
1. 取出入度为0的点
2. 删除该点输出的边
3. 循环直到没有为0的点，如果存在入度不为0的点，即有环

"""
from queue import Queue

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #0 is end & 1 is start
        if numCourses == 0:
            return True
        indegree = [0 for i in range(numCourses)]
        queue = Queue()
        edges = {}

        for pres in prerequisites:
            indegree[pres[0]] = indegree[pres[0]] +1
            if pres[1] in edges:
                edges[pres[1]].append(pres[0])
            else:
                edges[pres[1]] = [pres[0]]

        for i in range(numCourses):
            if indegree[i] == 0:
                indegree[i] = -1                
                queue.put(i)
        
        if queue.empty():
            return False
        
        while not queue.empty():
            cur = queue.get()
            fromEdges = edges.pop(cur,[])
            for end in fromEdges:
                indegree[end] = indegree[end]-1
            
            for i in range(numCourses):
                if indegree[i] == 0:
                    indegree[i] = -1
                    queue.put(i)
        
        for i in range(numCourses):
            if indegree[i] > 0:
                return(False)
        
        return(True)


        



        

