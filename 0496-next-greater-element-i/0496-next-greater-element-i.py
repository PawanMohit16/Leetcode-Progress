class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        res_arr = [-1] * n
        
        for i in range(n):
            j = 0
            unlock = False
            while j < m:
                if nums1[i] == nums2[j]:
                    unlock = True
            
                if unlock and nums2[j] > nums1[i]:
                    res_arr[i] = nums2[j]
                    break

                j += 1

        return res_arr
