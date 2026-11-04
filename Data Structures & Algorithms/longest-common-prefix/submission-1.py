class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(longest_prefix):
                longest_prefix = longest_prefix[:-1]

                
        return longest_prefix


        