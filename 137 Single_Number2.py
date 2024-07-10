class Solution:
    def same_len(self,num,max_len):
        sub_str = "0"*(max_len - ( len( bin( num ) )-2 ) )
        return bin(num).replace("0b", sub_str)

    def singleNumber(self, nums) -> int:
        final_ans = 0
        count = 0
        max_val = 0
        neg_count = 0

        for i in nums:
            if i < 0:
                i = -i
                neg = True
            max_val = max(i,max_val)
    
        length = len(bin(max_val))-2 if not neg else len(bin(max_val))-1

        j = 0
        while j < length:
            count = 0
            for i in nums:
                if self.same_len(i,length)[-1+(-1*j)] == '1':
                    count += 1
                if self.same_len(i,length)[-1+(-1*j)] == '-':
                    neg_count += 1
            if count%3 != 0:
                final_ans += 2**(j)
            j+=1
        if neg_count % 3 != 0:
            final_ans = -final_ans
        print(final_ans)
if __name__ == "__main__":
    s = Solution()
    s.singleNumber([-2,-2,1,1,4,1,4,4,-4,-2])