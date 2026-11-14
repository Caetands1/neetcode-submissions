class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        res = []
        for i in nums:
            if i in num_count:
                num_count[i] += 1
            else:
                num_count[i] = 1 
        sorted_nums = sorted(num_count, key = num_count.get, reverse=True)
        for i in range(k):
            res.append(sorted_nums[i])

        return res
