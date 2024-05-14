
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # check which string is larger
        if min(len(str1), len(str2)) == len(str1):
            smaller = str1; larger = str2
        else: 
            smaller = str2; larger = str1

        gcd = ""
        for j in range(len(smaller)):
            temp = smaller[0:j+1]
            mod_1 = len(larger) % len(temp)
            mux_1 = int(len(larger) / len(temp))
            mod_2 = len(smaller) % len(temp)
            mux_2 = int(len(smaller) / len(temp))
           
            if (mod_1 == 0) & (larger == temp * mux_1) & (mod_2 == 0) & (smaller == temp * mux_2):
                gcd = temp

        return gcd

    # A better solution using recursion
    # Time complexity O(n), Space complexity O(n)
    def gcdOfStrings_BETTER(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])