# arr1 = [1,4,8]
# arr2 = [1,2,3,4,7,10,10]
# Difficulty: Medium
def two_sorted_array(arr1, arr2):
    i = len(arr1)-1
    j = len(arr2)-1
    s_set = set()
    temp = 0
    for m in range(len(arr2)-1, -1, -1):
        if arr2[m]>arr1[i]:
            if arr2[m] not in s_set:
                s_set.add(arr2[m])
                
            elif arr2[m] in s_set and arr1[i] not in s_set:
                temp = arr1[i]
                arr1[i] = arr2[m]
                arr2[m] = temp
                s_set.add(arr2[m])
                i -= 1
                
            elif arr2[m] in s_set and arr1[i] in s_set:
                i -= 1
                
        elif arr1[i] > arr2[m]:
            if arr1[i] not in s_set:
                temp = arr1[i]
                arr1[i] = arr2[m]
                arr2[m] = temp
                s_set.add(arr2[m])
                
            elif arr1[i] in s_set and arr2[m] not in s_set:
                s_set.add(arr2[m])
                
            elif arr1[i] in s_set and arr2[m] in s_set:
                i -= 1
        
        elif arr2[m] == arr1[i]:
            if arr2[m] not in s_set:
                s_set.add(arr2[m])
                i -= 1
            elif arr2[m] in s_set:
                while arr1[i] == arr2[m]:
                    i -= 1
                temp = arr1[i]
                arr1[i] = arr2[m]
                arr2[m] = temp
                s_set.add(arr2[m])
                i -= 1
                

arr1 = [1,2,2,2,2,2,3,3,3,3,3,4,6,8,11]
arr2 = [1,3,4,7,7,10,10,10,10]
two_sorted_array(arr1, arr2)
print(sorted(arr2))