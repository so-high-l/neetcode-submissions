class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        seen = set()
        res = []
        nums2 = set(nums2)
        for i in range(len(nums1)):
            if not nums1[i] in seen and nums1[i] in nums2:
                seen.add(nums1[i])
                res.append(nums1[i])
        return res

        