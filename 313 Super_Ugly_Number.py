class Solution:
    # def nthSuperUglyNumber(self, n: int, primes) -> int:
    #     def check_primes(num):
    #         count_p = 0
    #         while num >= 1:
    #             if count_p > len(primes)-1:
    #                 break
    #             if num%primes[count_p] == 0:
    #                 num = num/primes[count_p]
    #             else:
    #                 count_p += 1
    #         if num == 1:
    #             return True
    #         else: return False
    #     count = 1
    #     i = 1
    #     while count < n:
    #         i += 1
    #         if check_primes(i):
    #             count += 1
    #     return i 

        def nthSuperUglyNumber(self, n: int, primes) -> int:
            arr = [float('inf')]*n
            arr[0] = 1
            last = [1]*len(primes)
            for i in range(1,n):
                for j in arr[max(0,i-n):i]:
                    for k in primes:
                        if j*k not in arr:
                            arr[i] = min(arr[i], j*k)
                    
            return arr[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.nthSuperUglyNumber(12,[2,7,13,19]))