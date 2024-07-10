class MinStack:
    class Node:
        def __init__(self,val=0,min_val=0):
            self.val = val
            self.min_val = min_val

    def __init__(self):
        self.stack_arr = []


    def push(self, val: int) -> None:
        if len(self.stack_arr) != 0:
            min_val = self.stack_arr[-1].min_val
        else:
            min_val = val
        node = self.Node(val,min(val,min_val))
        self.stack_arr.append(node)

    def pop(self) -> None:
        self.stack_arr.pop()

    def top(self) -> int:
        return self.stack_arr[-1].val

    def getMin(self) -> int:
        return self.stack_arr[-1].min_val
        
if __name__ =="__main__":
    m = MinStack()
    print(m.push(-2))
    print(m.push(0))
    print(m.push(-3))
    print(m.getMin())
    print(m.pop())
    print(m.top())
    print(m.getMin())