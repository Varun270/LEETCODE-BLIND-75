# Problem Link --> https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key= lambda x:x[0])
        ans = [intervals[0]]
        
        for start, end in intervals[1:]:
            
            localend = ans[-1][1]
            
            if start <= localend:
                ans[-1][1] = max(localend, end)
                
            else:
                ans.append([start, end])
                
        return ans