# My own solution:

class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))
        low = -1 * pow(2, 31)
        up = (pow(2, 31)) - 1
        x_str = ""
        for i in s:
            x_str = i + x_str

        if x < 0:
            if (-1 * int(x_str)) < low :
                return 0
            else:
                return -1 * int(x_str)

        else:
            if int(x_str) > up:
                return 0
            else:
                return int(x_str)
        
- Runtime: 42ms
- Memory: 16.24MB
-> Need to find a better solution