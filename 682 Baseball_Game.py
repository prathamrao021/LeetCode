class Solution:
    def calPoints(self, operations) -> int:
        arr = []
        for i in operations:
            if i.isdigit():
                arr.append(int(i))
            elif i[1:].isdigit():
                arr.append(int(i))
            elif i == "C":
                arr.pop()
            elif i == "D":
                arr.append(arr[-1]*2)
            elif i == "+":
                arr.append(arr[-1]+arr[-2])
        return sum(arr)

if __name__ == "__main__":
    s = Solution()
    print(s.calPoints(["-21","-66","39","+","+"]))