# MY SOLUTION
# class Solution:
#     def reach_curr_sta(self,gas,cost,starting_ind,curr_ind,gas_left):
#         #the gas left after using some to reach the current gas station
#         # print(starting_ind,curr_ind)
#         if curr_ind == starting_ind and gas_left >= 0:
#             return
#         gas_left += (gas[curr_ind])
#         print("gas left",gas_left)

#         if gas_left > 0:
#             self.result = True
#             # if curr_ind == starting_ind-1 and gas_left >= cost[curr_ind]:
#             #     return
#             if gas_left >= cost[curr_ind]:
#                 self.reach_curr_sta(gas,cost,starting_ind,curr_ind+1 if curr_ind < len(gas)-1 else 0,gas_left - cost[curr_ind])
#             else:
#                 self.result = False
#                 return
#         else:
#             self.result = False
#             return
#     def canCompleteCircuit(self, gas, cost):
#         ans = -1
#         self.result = True
#         check = True
#         for ind,ga_co in enumerate(zip(gas,cost)):
#             if ga_co[0] <= ga_co[1]:
#                 check = False
#         if check:
#             return 0

#         for ind,ga_co in enumerate(zip(gas,cost)):
#             if ga_co[0] >= ga_co[1]:
#                 self.reach_curr_sta(gas,cost,ind,ind+1 if ind < len(gas)-1 else 0,ga_co[0]-ga_co[1])
#                 if self.result:
#                     ans = ind
#                     break
#                 #  print(ind,ga_co)
#             # print(ind,ga_co[0],ga_co[1])
#         return(ans)



class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        if (sum(gas) - sum(cost) < 0):
            return -1
        
        gas_tank, start_index = 0, 0
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start_index = i+1
                gas_tank = 0
            
        return start_index
if __name__ == "__main__":
    s = Solution()
    # s.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])
    # k = s.canCompleteCircuit([5,1,2,3,4],[4,4,1,5,1])
    k = s.canCompleteCircuit([3,1,1],[1,2,2])

    print(k)

