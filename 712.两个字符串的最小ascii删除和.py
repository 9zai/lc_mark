#
# @lc app=leetcode.cn id=712 lang=python3
#
# [712] 两个字符串的最小ASCII删除和
#
import sys

class Solution:
    def search(self,s1:List[str],s2:List[str],cost:int):
        if str(s1)+str(s2) in self.paths.keys():
            if cost > self.paths.get(str(s1)+str(s2)):
                return()
        else:
            self.paths[str(s1)+str(s2)] = cost

        if len(s1) == 0 and len(s2) == 0:
            self.res = min(self.res,cost)
            return()
        if cost > self.res:
            return()
        
        if len(s1) == 0:
            rmvCost = ord(s2.pop(0))
            self.search(s1,s2,cost+rmvCost)
            s2.insert(0,chr(rmvCost))
            return()
        elif len(s2) == 0:
            rmvCost = ord(s1.pop(0))
            self.search(s1,s2,cost+rmvCost)
            s1.insert(0,chr(rmvCost))
            return()

        if s1[0] == s2[0]:
            match = s1.pop(0)
            s2.pop(0)
            self.search(s1,s2,cost)

            s1.insert(0,match)
            s2.insert(0,match)

        
        #remove from s1
        rmvCost = ord(s1.pop(0))
        self.search(s1,s2,cost+rmvCost)
        s1.insert(0,chr(rmvCost))

        rmvCost = ord(s2.pop(0))
        self.search(s1,s2,cost+rmvCost)
        s2.insert(0,chr(rmvCost))


        
        

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        self.res = sys.maxsize
        self.paths = {}

        self.search(list(s1),list(s2),0)

        return(self.res)
        

