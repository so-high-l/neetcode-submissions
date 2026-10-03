class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_tracker = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_tracker:
                return [nums_tracker[complement], i]
            nums_tracker[num] = i
