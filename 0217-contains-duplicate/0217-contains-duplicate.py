class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map=dict()
        for i in nums:
            if i in map:
                map[i]+=1
            else:
                map[i]=1
        values=list(map.values())
        for i in values:
            if i!=1:
                return True
        return False
        