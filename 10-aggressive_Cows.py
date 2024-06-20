class Solution:
    def solve(self,n,k,stalls):
        stalls.sort()
        maxi = stalls[n-1] - stalls[0]
        mini = stalls[1] - stalls[0]
        
        for index in range(2,n):
            mini = min(mini, stalls[index]- stalls[index-1])
            
        
        def ispossible(val):
            cowtoplace = k-1
            prev = 0
            
            for index in range(1,n):
                diff = stalls[index] - stalls[prev]
                if diff >= val:
                    prev = index
                    cowtoplace -=1
                    if cowtoplace == 0:
                        return True
            return False
            
        
        res = -1
        left, right = mini, maxi
        while left <= right:
            mid = (left+right) // 2
            if ispossible(mid):
                res = mid
                left = mid+1
            else:
                right = mid-1
        return res
