import collections
class Solution:
    def intersect(self, nums1, nums2):
        list1 = collections.Counter(nums1)
        list2 = collections.Counter(nums2)
        ans = []
        for i in list1.keys():
            if list2.get(i) != None:
                min_num = min(list1[i], list2[i])
                for j in range(min_num):
                    ans.append(i)
        return(ans)
if __name__ == "__main__":
    s = Solution()
    k = s.intersect([1,2,2,1],[2,2])
    print(k)