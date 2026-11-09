class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best_length = 0 
        seen = set(nums)

        for num in seen:
            length = 1
            next_item = num + 1

            if not num - 1 in seen:
                while next_item in seen:
                    length += 1
                    next_item += 1

            best_length = max(best_length, length)

        return best_length

        

