import collections
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        all_set = set([0,x,y,x+y,abs(x-y)])
        temp_set = set()
        intersection_que = collections.deque([abs(x-y)])
        max_pos = x+y

        while True:
            temp_set = set()
            new = intersection_que.popleft()
            for i in all_set:
                if new +i <= max_pos:
                    temp_set.add(new+i)
                temp_set.add(abs(new-i))
            intersection_que += list(temp_set ^ all_set)
            temp_set = all_set.union(temp_set)
            if target in temp_set:
                return True
            if len(temp_set) == len(all_set):
                return False
            all_set = temp_set

if __name__ == "__main__":
    s = Solution()
    print(s.canMeasureWater(34,5,6))