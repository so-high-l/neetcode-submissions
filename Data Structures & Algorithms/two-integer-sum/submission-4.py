class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_sum = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in diff_sum:
                return [diff_sum[complement], i]
            diff_sum[num] = i
