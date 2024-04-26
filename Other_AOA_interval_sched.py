class lecture:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

class Solution:
    def interval_scheduling(self):
        lec1 = lecture("A", 0, 6)
        lec2 = lecture("B", 1, 4)
        lec3 = lecture("C", 3, 5)
        lec4 = lecture("D", 3, 8)
        lec5 = lecture("E", 4, 7)
        lec6 = lecture("F", 5, 9)
        lec7 = lecture("G", 6, 10)
        lec8 = lecture("H", 8, 11)

        all_lec = [lec1, lec2, lec3, lec4, lec5, lec6, lec7, lec8]
        all_lec.sort(key=lambda x:x.end)

        running_time = 0
        maximum = max(all_lec, key=lambda x:x.end).end

        final_list = []
        for i in all_lec:
            if i.start >= running_time:
                final_list.append(i)
                running_time = i.end
            if running_time >= maximum:
                break
        self.print_lecture(final_list)
            
    def print_lecture(self, lectures):
        print("Lecture name\tstart\tend")
        for i in lectures:
            print(str(i.name)+"\t"+str(i.start)+"\t"+str(i.end))

if __name__ == "__main__":
    s = Solution()
    s.interval_scheduling()