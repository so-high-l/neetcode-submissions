class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:  
        current_sum = 0
        prefix_count = { 0 : 1 }
        answer = 0

        for num in nums:
            current_sum += num
            needed = current_sum - k

            if needed in prefix_count:
                answer += prefix_count.get(needed, 0)
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return answer



