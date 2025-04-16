class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        result = []
        for n in nums2:
            index = bisect.bisect_left(nums1, n)
            if index < len(nums1) and nums1[index] == n and n not in result:
                result.append(n)
        return result
