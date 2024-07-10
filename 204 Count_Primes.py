class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n ==1 : return 0
        arr = [True]*n
        arr[0],arr[1] = False, False

        for i in range(2, int(n**(0.5))+1):
            if arr[i]:
                for j in range(i+i,n,i):
                    arr[j] = False
        return sum(arr)

if __name__ =="__main__":
    s = Solution()
    k = s.countPrimes(10)
    print(k)