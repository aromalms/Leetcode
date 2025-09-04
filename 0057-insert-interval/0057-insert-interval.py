class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n=len(intervals)
        res=[]
        for i in range(n):
            start,end=intervals[i]
            if newInterval[1]<start:
                res.append(newInterval)
                return res+intervals[i:]
            elif newInterval[0]>end:
                res.append(intervals[i])
            else:
                newInterval[0]=min(start,newInterval[0])
                newInterval[1]=max(end,newInterval[1])
        res.append(newInterval)
        return res
        
                