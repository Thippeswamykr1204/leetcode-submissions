class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # By using arrays
        # freq = {}      

        # for i in nums:
        #     freq[i] = freq.get(i, 0) + 1

        # for i in freq:
        #     if freq[i] == 1:
        #         return i

        # By using Bit Manipulations
        result = 0
        for i in nums:
            result ^= i 
        return result