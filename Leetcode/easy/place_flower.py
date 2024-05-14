from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # extend our array on two edges for easier check in the loop
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed)-1):
            if n == 0:
                break
            if (flowerbed[i-1] ==0) and (flowerbed[i] == 0) and (flowerbed[i+1] ==0):
                flowerbed[i] = 1
                n -= 1
    
        return n <= 0