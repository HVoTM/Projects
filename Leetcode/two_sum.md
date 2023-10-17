```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # answer to return
        ans = []

        # dictionaries for indices for the difference in each indices
        difference_chart = {}

        # iterate over via enumerate(), so we can derive both indices and corresponding values
        for i, n in enumerate(nums):
            # Check the difference
            diff = target - n
            if diff in difference_chart:
                ans.append(i)
                ans.append(difference_chart[diff])
                break
            else:
                difference_chart[n] = i
        return ans
```