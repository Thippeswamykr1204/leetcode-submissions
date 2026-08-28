class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        n = len(nums)
        missing = 0
        duplicate = 0

        for i in range(1, n+1):
            if i not in count:
                missing = i
            elif count[i] == 2:
                duplicate = i

        return [duplicate, missing]