from typing import List

def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # find the kids with the greatest number of candies
        max_candies = max(candies)

        # init a bool return array
        most_candies = [False for i in range(len(candies))]

        for j in range(len(candies)):
            if candies[j] + extraCandies >= max_candies:
                most_candies[j] = True
        return most_candies