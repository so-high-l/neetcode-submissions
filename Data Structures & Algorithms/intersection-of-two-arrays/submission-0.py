class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        seen = set()
        res = []
        for i in range(len(nums1)):
            if not nums1[i] in seen and nums1[i] in nums2:
                print("adding ", nums1[i])
                seen.add(nums1[i])
                res.append(nums1[i])

        for i in range(len(nums2)):
            if not nums2[i] in seen and nums2[i] in nums1:
                seen.add(nums2[i])
                print("adding ", nums2[i])
                res.append(nums1[i])
        return res

        