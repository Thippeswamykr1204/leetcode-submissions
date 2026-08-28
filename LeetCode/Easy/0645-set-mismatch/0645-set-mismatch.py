class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        nums.sort()
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                result.append(nums[i])

        for i in range(1, n+1):
            if i not in nums:
                result.append(i)

        return result