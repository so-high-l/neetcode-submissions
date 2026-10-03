class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        for word in strs:
            counts = [0] * 26

            for letter in word:
                counts[ord(letter) - ord('a')] += 1

            grouped.setdefault(tuple(counts), []).append(word)

        return list(grouped.values())