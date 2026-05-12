class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        l1 = nums1 + nums2
        l = sorted(l1)
        leng = len(l)

        if leng % 2 != 0:
            ans = (leng // 2)
            return l[ans]

        elif leng % 2 == 0:
            ans = (l[leng // 2] + l [(leng // 2) - 1]) / 2.0
            return ans

        