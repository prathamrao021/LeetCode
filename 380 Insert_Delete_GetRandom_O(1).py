import random
class RandomizedSet:

    def __init__(self):
        self.array = []
        self.hashtable = dict()

    def insert(self, val: int) -> bool:
        if self.hashtable.get(val) != None:
            return False
        self.array.append(val)
        self.hashtable[val] = len(self.array)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashtable:
            return False
        
        remov_ind = self.hashtable[val]
        last_element = self.array[-1]
        
        self.array[remov_ind] = last_element
        self.hashtable[last_element] = remov_ind
        
        self.array.pop()
        del self.hashtable[val]
        
        return True

    def getRandom(self) -> int:
        return self.array[random.randrange(0, len(self.array))]

if __name__ == "__main__":

    arr_op = ["insert","insert","remove","insert","insert","insert","remove","remove","insert","remove","insert","insert","insert","insert","insert","getRandom","insert","remove","insert","insert"]
    arr_num = [[3],[-2],[2],[1],[-3],[-2],[-2],[3],[-1],[-3],[1],[-2],[-2],[-2],[1],[],[-2],[0],[-3],[1]]
    s = RandomizedSet()

    for i in range(len(arr_op)):
        operation = arr_op[i]
        if operation == "insert":
            print(f"insert({arr_num[i][0]}) -> {s.insert(arr_num[i][0])}")
        elif operation == "remove":
            print(f"remove({arr_num[i][0]}) -> {s.remove(arr_num[i][0])}")
        elif operation == "getRandom":
            print(f"getRandom() -> {s.getRandom()}")
