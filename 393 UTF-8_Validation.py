class Solution:
    def validUtf8(self, data) -> bool:
        def conv(n):
            s = bin(n)[2:]
            s = '0'*(8-len(s))+s
            # print(s)
            return s
        
        bit4 = '11110'
        bit3 = '1110'
        bit2 = '110'
        bit1 = '0'
        cbit = '10'
        i = 0
        while i<len(data):
            if conv(data[i]).startswith(bit4):
                i += 1
                if i<len(data) and conv(data[i]).startswith(cbit):
                    i += 1
                    if i<len(data) and conv(data[i]).startswith(cbit):
                        i += 1
                        if i<len(data) and conv(data[i]).startswith(cbit):
                            i += 1
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            elif conv(data[i]).startswith(bit3):
                i += 1
                if i<len(data) and conv(data[i]).startswith(cbit):
                    i += 1
                    if i<len(data) and conv(data[i]).startswith(cbit):
                        i += 1
                    else:
                        return False
                else:
                    return False
            elif conv(data[i]).startswith(bit2):
                i += 1
                if i<len(data) and conv(data[i]).startswith(cbit):
                    i += 1
                else:
                    return False
            elif conv(data[i]).startswith(bit1):
                i+=1
            else:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.validUtf8([228,189,160,229,165,189,13,10]))