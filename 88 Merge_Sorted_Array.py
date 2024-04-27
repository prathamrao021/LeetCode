class Solution:
    def swap(self, nums1,nums2,i,j):
        temp = nums1[i]
        nums1[i] = nums2[j]
        nums2[j] = temp
    
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        no_changes = len(nums1)-m
        if m == 0:
            for i in range(len(nums2)):
                nums1[i]=nums2[i]
            # return
        elif n == 0:
            pass
            # return
        else:
            i = len(nums1)-1
            j = len(nums2)-1

            while no_changes > 0:
                if nums1[i] < nums2[j] or nums1[i] == 0:
                    self.swap(nums1, nums2, i, j)
                    no_changes -= 1
                if nums2[j] == 0 and j>0:
                    j -= 1
                i -= 1
            # nums1 = sorted(nums1)
            
            if nums1[i] > nums1[i+1]:
                self.swap(nums1, nums1, i, i+1)
        print(nums1)


s = Solution()
s.merge([0,0,3,0,0,0,0,0,0],3,[-1,1,1,1,2,3],6)