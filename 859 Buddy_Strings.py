class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        start = 0
        end = 0
        s = list(s)
        goal = list(goal)
        for i in range(len(goal)):
            if s[i] != goal[i]:
                start = i
                break
        for i in range(len(goal)-1,-1,-1):
            if s[i] != goal[i]:
                end = i
                break
        
        s[start], s[end] = s[end], s[start]
        # goal[start], goal[end] = goal[end], goal[start]

        s = " ".join(s)
        goal = " ".join(goal)
        
        return s == goal

if __name__ == "__main__":
    s = Solution()
    print(s.buddyStrings('ab','ba'))