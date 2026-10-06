class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best_length = 0
        nums_set = set(nums)

        for num in nums:
            if num-1 not in nums_set:
                current = num
                count = 1
                while current+1 in nums_set:
                    count += 1
                    current += 1
                
                best_length = max(count, best_length)
        
        return best_length