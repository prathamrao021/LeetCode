import collections
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        count_table = collections.Counter(nums)

        print(count_table)
        max_heap = []
        for i in count_table.keys():
            heapq.heappush(max_heap,(-count_table[i],i))
        final_ans = []
        for i in range(k):
            final_ans.append(heapq.heappop(max_heap)[1])
        return final_ans
if __name__ == "__main__":
    s = Solution()
    k = s.topKFrequent([1,1,1,2,2,3],2)
    print(k)
        

