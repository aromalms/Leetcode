class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        new_map=dict()
        for i,num in enumerate(nums):
            if num in new_map and i-new_map[num]<=k:
                return True
            new_map[num]=i
        return False