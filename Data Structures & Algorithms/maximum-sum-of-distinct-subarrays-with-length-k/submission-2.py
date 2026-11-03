class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if k > len(nums) or k <= 0:
            return None
        
        previous_sum = 0
        best_sum = 0

        left = 0
        right = k 

        freq = {}
        
        for i in range(k):
            previous_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        if len(freq) == k:
            best_sum = previous_sum



        while(right < len(nums)):
            # print("Previous map: ", freq)
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]

            freq[nums[right]] = freq.get(nums[right], 0) + 1
            # print("New map: ", freq)
            previous_sum = previous_sum - nums[left] + nums[right]
            if(len(freq) == k):
                best_sum = max(previous_sum, best_sum)

            right += 1
            left += 1
        return best_sum
            





