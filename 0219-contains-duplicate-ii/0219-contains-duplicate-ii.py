class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup_set = {}
        for i, num in enumerate(nums):
            if num in dup_set:
                if i - dup_set[num] <= k:
                    return True
            dup_set[num] = i
        return False