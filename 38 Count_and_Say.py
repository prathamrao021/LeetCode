class Solution:
    def get_string_for_num(self,num,count_arr,counter,number):
        if num == 1:
            return "1"
        if num > 1:
            self.number = self.get_string_for_num(num-1,count_arr,counter,number)

            string_num = str(self.number)
            # print(num)
            count_arr = []
            for i in string_num:
                try:
                    if count_arr[-1][0] == int(i):
                        count_arr[-1][1] += 1
                    else:
                        count_arr.append([int(i),1])
                except:
                     count_arr.append([int(i),1])
            
            new_string = ""
            for i, j in count_arr:
                 new_string += str(j)+str(i)
            # print(new_string)
            return new_string


        
    def countAndSay(self, n: int) -> str:
        counter = 0
        count_arr = {}
        number = 0
        self.get_string_for_num(n, count_arr, counter, number)


if __name__ == "__main__":
    s = Solution()
    l = {}
    k = s.get_string_for_num(5,l,0,0)
    print(k)



# def get_string_for_num(num,count_arr,counter,number):
#         if num == 1:
#             return 1
#         if num > 1:
#             number = get_string_for_num(num-1,count_arr,counter,number)

#             string_num = str(number)
#             print(num)
#             count_arr = []
#             for i in string_num:
#                 try:
#                     if count_arr[-1][0] == int(i):
#                         count_arr[-1][1] += 1
#                     else:
#                         count_arr.append([int(i),1])
#                 except:
#                      count_arr.append([int(i),1])
            
#             new_string = ""
#             for i, j in count_arr:
#                  new_string += str(j)+str(i)
#             print(new_string)
#             return new_string
            
            

# print(get_string_for_num(5,[],0,0))