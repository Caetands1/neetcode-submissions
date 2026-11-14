from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(list)
        count = 0 
        res = []
        for i in nums:
            if i in num_count:
                num_count[i] += 1
            else:
                num_count[i] = 1 
        for i in range(k):
            res.append(sorted(num_count, key = num_count.get, reverse=True)[i])

        return res
