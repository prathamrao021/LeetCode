class Solution:
    def calculate(self, arr, ind):
        if ind >= len(arr):
            self.check = False
            return ind
        if arr[ind].isdigit():
            #left
            ind = self.calculate(arr,ind+1)
            #right
            ind = self.calculate(arr,ind+1)  
        return ind
    def isValidSerialization(self, preorder: str) -> bool:
        tree_arr = preorder.split(',')
        self.check = True

        print(tree_arr)
        index = self.calculate(tree_arr,0)
        if index == len(tree_arr)-1:
            return self.check
        else:
            return False
if __name__ == "__main__":
    s = Solution()
    print(s.isValidSerialization("1,#"))