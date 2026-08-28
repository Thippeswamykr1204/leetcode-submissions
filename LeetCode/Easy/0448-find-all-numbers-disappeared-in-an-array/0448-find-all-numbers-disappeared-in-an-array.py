class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        n = len(nums)
        result = []

        for i in range(1, n+1):
            if i not in seen:
                result.append(i)

        return result