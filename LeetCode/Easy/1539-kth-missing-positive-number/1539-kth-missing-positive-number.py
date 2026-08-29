class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        num = 1
        i = 0

        while len(missing) < k:
            if i < len(arr) and arr[i] == num:
                i += 1
            else:
                missing.append(num)
            num += 1

        return missing[-1]