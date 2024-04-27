class Solution:
    def markup_language(self, s):
        ans = ""
        title = 0
        subtitle = 0
        data = s.split("\n")
        # print(data)
        for i in range(len(data)):
            if '##' in data[i]:
                subtitle += 1
                subtitle_name = data[i].split(" ")
                if len(subtitle_name) == 2:
                    subtitle_name = (subtitle_name[1])
                    ans += str(title)+"."+str(subtitle)+" "+str(subtitle_name)+"\n"
                else:
                    sub_name = ""
                    for i in subtitle_name:
                        if i != "##":
                            sub_name += i+" "
                    ans += str(title)+"."+str(subtitle)+" "+str(sub_name)+"\n"
            elif "#" in data[i]:
                title += 1
                subtitle = 0
                title_name = data[i].split(" ")
                if len(title_name) == 2:
                    title_name = (title_name[1])
                    ans += str(title)+"."+" "+str(title_name)+"\n"
                else:
                    t_name = ""
                    for i in title_name:
                        if i != "#":
                            t_name += i+" "
                    
                    ans += str(title)+"."+" "+str(t_name)+"\n"
        print(ans)
if __name__ == "__main__":
    s = Solution()
    s.markup_language("""
# Algorithms
This chapter covers the most basic algorithms.
## Sorting
Quicksort is fast and widely used in practice
Merge sort is a deterministic algorithm
## Searching
DFS and BFS are widely used graph searching algorithms
Some variants of DFS are also used in game theory applications
# Data Structures
This chapter is all about data structures
It's a draft for now and will contain more sections in the future
## Don't Know
# Binary Search Trees
This is the table of contents that must be produced:
""")