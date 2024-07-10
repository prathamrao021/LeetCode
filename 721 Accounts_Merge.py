from collections import defaultdict
class Solution:
    def dfs(self,node,adjacent_matrix,visit):
        visit.add(node)
        for neighbor in adjacent_matrix[node]:
            if neighbor not in visit:
                self.dfs(neighbor,adjacent_matrix,visit) 
        self.result.append(node)
    def accountsMerge(self, accounts):
        adjacent_matrix = defaultdict(set)
        for account in accounts:
            for emails in account[1:]:
                adjacent_matrix[account[1]].add(emails)
                adjacent_matrix[emails].add(account[1])
        # print(adjacent_matrix)
        visit = set()
        final_ans = []

        for account in accounts:
            
            for email in account[1:]:
                if email not in visit:
                    self.result = list()
                    self.dfs(email,adjacent_matrix,visit)
                    print(self.result)
                    final_ans.append([account[0]]+sorted(self.result))
        return(final_ans)

if __name__ == "__main__":
    s = Solution()
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    k = s.accountsMerge(accounts)
    print(k)