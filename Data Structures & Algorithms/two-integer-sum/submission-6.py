class Solution:
    def twoSum(self, nums: list[int], target: int):

        seen = {}
        result = []

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                result = [seen[complement], i]
            else:
                seen[nums[i]] = i
        return result
 