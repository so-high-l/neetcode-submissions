class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)

        for word in strs:
            counts = [0] * 26

            for char in word:
                counts[ord(char) - ord('a')] += 1
            
            grouped[tuple(counts)].append(word)

        return list(grouped.values())