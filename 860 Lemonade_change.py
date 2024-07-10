class Solution:
    def lemonadeChange(self, bills) -> bool:
        b_dict = {5:0,10:0}

        for i in bills:
            if i == 5:
                b_dict[i] += 1
            elif i == 10:
                b_dict[i] += 1
                if b_dict[5] > 0:
                    b_dict[5] -= 1
                else:
                    return False
            elif i == 20:
                if b_dict[10] > 0:
                    b_dict[10] -= 1
                    if b_dict[5] > 0:
                        b_dict[5] -= 1
                    else:
                        return False
                else:
                    if b_dict[5] >= 3:
                       b_dict[5] -= 3
                    else:
                        return False 
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.lemonadeChange([5,5,10,10,20]))