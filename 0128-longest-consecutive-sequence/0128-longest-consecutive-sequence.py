class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        current = 1
        longest = 1
        n = len(nums)
        
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    current += 1
                else:
                    longest = max(current, longest)
                    current = 1 

        return max(current, longest)