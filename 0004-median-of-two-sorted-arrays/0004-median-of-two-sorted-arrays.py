class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mer=nums1+nums2
        mer.sort()
        total=len(mer)
        if total % 2 == 1:
            return float(mer[total//2])
        else:
            mid1=mer[total // 2 - 1]
            mid2=mer[total // 2]
            return (float(mid1) + float(mid2)) / 2.0

