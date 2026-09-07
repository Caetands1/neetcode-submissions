class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       nums_prev = {}
       for i, n in enumerate(nums):
        print(i,n)
        diff = target - n
        if diff in nums_prev:
            return [nums_prev[diff], i]
        else:
            nums_prev[n] = i
