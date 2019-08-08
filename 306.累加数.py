#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return(False)
        for i in range(1,n-1):
            for j in range(i+1,n):
                if num[i] == '0' and (j-i)>1:
                    continue
                a = num[0:i]
                b = num[i:j]

                isValid = self.check(num,a,b,j)
                if isValid:
                    return(True)
        return(False)

    def add(self,a:str,b:str) ->str:
        #supposed a <= b
        lenA = len(a)
        lenB = len(b)
        isAddOne = False
        res = ""
        i=1
        while i <= lenA:
            intA = int(a[-i])
            intB = int(b[-i])

            val = intA + intB
            if isAddOne:
                isAddOne = False
                val+=1
            if val >=10:
                isAddOne = True
                val-=10
            res = str(val)+res

            i+=1
        
        while i <= lenB and isAddOne:
            isAddOne = False
            val = int(b[-i])+1
            if val >=10:
                isAddOne = True
                val-=10
            res = str(val)+res
            i+=1
        
        
        if isAddOne:
            res = '1'+res
        elif i <= lenB:
            res = b[:-i+1] + res

        return(res)
        
            

    def check(self,num:str,a:str,b:str,index:int) ->bool:
        if index == len(num):
            return(True)
    
        if len(a) > len(b):
            ta = b
            tb = a
        else:
            ta = a
            tb = b
        res = self.add(ta,tb)

        if index + len(res) > len(num):
            return(False)
        else:
            match = num[index:index+len(res)]
            if match == res:
                if index + len(res) < len(num) and num[index + len(res)] !='0':
                    return(self.check(num,b,res,index+len(res)))
                elif index + len(res) == len(num):
                    return(True)
                else:
                    return(False)
            else:
                return(False)
            



