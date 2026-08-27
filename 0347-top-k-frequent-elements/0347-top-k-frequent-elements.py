class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        unique_ele = list(set(nums))

        for num in unique_ele:
            freq.append((num, nums.count(num)))
        freq.sort(key = lambda X:X[1], reverse=True)

        return [freq[i][0] for i in range(k)]