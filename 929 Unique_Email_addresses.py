import re
class Solution:
    def numUniqueEmails(self, emails) -> int:
        set_email = set()
        for i in range(len(emails)):
            a_split = emails[i].split('@')
            correct_name = a_split[0].split('+')
            name = re.sub(r'\.','',correct_name[0])

            set_email.add(name+'@'+a_split[1])
        return len(set_email)
    
if __name__ == "__main__":
    s = Solution()
    print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]))