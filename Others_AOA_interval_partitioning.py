class lecture:
    def __init__(self, name, start, end, selected=False):
        self.name = name
        self.start = start
        self.end = end
        self.selected = selected

class Solution:
    def interval_partitioning(self):
        lec1 = lecture("A", 9, 10.30)
        lec2 = lecture("B", 9, 12.30)
        lec3 = lecture("C", 9, 10.30)
        lec4 = lecture("D", 11, 12.30)
        lec5 = lecture("E", 11, 14)
        lec6 = lecture("F", 13, 14.30)
        lec7 = lecture("G", 13, 14.30)
        lec8 = lecture("H", 14, 16.30)
        lec9 = lecture("I", 15, 16.30)
        lec10 = lecture("J", 15, 16.30)

        all_lec = [lec1, lec2, lec3, lec4, lec5, lec6, lec7, lec8, lec9, lec10]
        all_lec.sort(key=lambda x:x.start)

        running_time = 0
        maximum = max(all_lec, key=lambda x:x.end).end
        selected_lec = set()
        classroom = []
        total_classroom = []
        
        while len(selected_lec) != len(all_lec):
            running_time = 0
            for i in range(len(all_lec)):
                if all_lec[i] not in selected_lec and (all_lec[i].start >= running_time or i == 0):
                    classroom.append(all_lec[i])
                    running_time  = all_lec[i].end
                    selected_lec.add(all_lec[i])
            total_classroom.append(classroom.copy())
            classroom.clear()
        
        self.print_lecture(total_classroom)
    
    def print_lecture(self, total_classroom):
        for lectures in range(len(total_classroom)):
            print("Classroom "+str(lectures+1))
            print("Lecture name\tstart\tend")
            for j in total_classroom[lectures]:
                print(str(j.name)+"\t\t"+str(j.start)+"\t"+str(j.end))

if __name__ == "__main__":
    s = Solution()
    s.interval_partitioning()
