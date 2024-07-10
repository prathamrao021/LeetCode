class Solution:
    def valid_sub_ip(self, s, sub_ip, num, length):
        if int(sub_ip) <= 255 and len(sub_ip) <= 3 and (num-1)*3 >= len(s)-length >= num-1:
            return 1
        else:
            return 0
        
    def to_get_first_sub_ip(self, s, sec_third_fourth_ip, int_ans, ans):
        first_ip = ''
        first_int_ip = int_ans
        for i in range((len(s)-len(sec_third_fourth_ip)-1),-1,-1):
                first_ip =  s[i] + first_ip
                if s[i] != '0' or first_ip == '' or first_ip == '0':
                    if self.valid_sub_ip(s, first_ip, 1, len(first_ip+sec_third_fourth_ip)):
                        int_ans = first_ip +"."+first_int_ip
                        ans.append(int_ans)
        return ans
                        # self.to_get_first_sub_ip(s, first_ip+sec_third_fourth_ip)


    def to_get_second_sub_ip(self, s, third_fourth_ip, int_ans, ans):
        second_ip = ''
        sec_int_ans = int_ans
        for i in range((len(s)-len(third_fourth_ip)-1),-1,-1):
            second_ip =  s[i] + second_ip
            if s[i] != '0' or second_ip == '' or second_ip == '0':
                if self.valid_sub_ip(s, second_ip, 2, len(second_ip+third_fourth_ip)):
                    int_ans = second_ip +"."+sec_int_ans
                    # print(int_ans)
                    ans = self.to_get_first_sub_ip(s, second_ip+third_fourth_ip, int_ans, ans)
        return ans
                    
    def to_get_third_sub_ip(self, s, fourth_sub_ip, int_ans, ans):
        third_sub_ip = ''
        for i in range((len(s)-len(fourth_sub_ip)-1),-1,-1):
            third_sub_ip =  s[i] + third_sub_ip
            if s[i] != '0' or third_sub_ip == '' or third_sub_ip == '0':
                if self.valid_sub_ip(s, third_sub_ip, 3, len(third_sub_ip+fourth_sub_ip)):
                    int_ans = third_sub_ip +"."+fourth_sub_ip
                    # print(int_ans)
                    ans = self.to_get_second_sub_ip(s, third_sub_ip+fourth_sub_ip, int_ans, ans)
        return ans

    def restoreIpAddresses(self,s):
        fourth_sub_ip = ''
        int_ans = ''
        ans = []
        for i in range(len(s)-1,-1,-1):
            fourth_sub_ip =  s[i] + fourth_sub_ip
            if s[i] != '0' or fourth_sub_ip == '' or fourth_sub_ip == '0':
                if self.valid_sub_ip(s, fourth_sub_ip, 4, len(fourth_sub_ip)):
                    int_ans = fourth_sub_ip
                    # print(int_ans)
                    ans = self.to_get_third_sub_ip(s, fourth_sub_ip, int_ans, ans)
        return ans
            

if __name__ == "__main__":
    s = Solution()
    print(s.restoreIpAddresses("101023"))