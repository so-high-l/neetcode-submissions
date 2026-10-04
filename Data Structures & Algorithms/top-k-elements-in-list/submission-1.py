class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        # Sort by value desc
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        for key, value in sorted_freq.items():
            result.append(key)

        return result[:k]


        
