class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split(".")
        arr2 = version2.split(".")

        max_length = max(len(arr1),len(arr2))
        arr1 = arr1 + ["0"]*(max_length-len(arr1))
        arr2 = arr2 + ["0"]*(max_length-len(arr2))
        # print(arr1,arr2)

        for i in range(len(arr2)):
            if int(arr1[i]) > int(arr2[i]):
                return 1
            elif int(arr2[i]) > int(arr1[i]):
                return -1
        return 0   


if __name__ == "__main__":
    s = Solution()
    s.compareVersion("1.001","1.01.00.0.0")
