import collections
import heapq
import re
with open("words.txt",'r') as f:
    s = f.read()
    s = re.sub(' +',' ',s)
    arr = s.split(" ")

    freq_table = collections.Counter(arr)
    max_heap = []
    for i in freq_table.keys():
        heapq.heappush(max_heap,(-freq_table[i],i))
    ans = ""

    for j in range(len(freq_table)):
        curr = heapq.heappop(max_heap)
        if j < len(freq_table)-1:
            ans += str(curr[1])+"  "+str(-curr[0])+"\n"
        else:
            ans += str(curr[1])+"  "+str(-curr[0])
    print(ans)