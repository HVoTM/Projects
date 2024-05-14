from typing import List
# NOTE: for reference: https://www.youtube.com/watch?v=aayNRwUN3Do
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            """EXPLANATION
            we will perform a swap between the two elements if the right element is not zero
            1. l=r points to index 0, r traverses through the list
            2. if r meets a zero, it will go over the next index
            3. any non-zero encountered by r will be swapped with the current residing left element
                - at the start the indexes of l and r are the same, basically we just swap with that 
                index itself internally.
                - after swapping, increment l by 1, that way, we will not intervene with the previously placed index
                preserving the original order
                - in other words, l will point to 0 and swap while r traverses to find the non-zero, swap,
                then go over the the remaining of the list


            # Draw out the thinking process to understand if you need some revision
            """
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    temp = []
    " THIS IS THE COPY ARRAY METHOD"    
    n = 0
    print(len(nums))
    for i in range(len(nums)):
        print(i)
        if nums[i] == 0:
            n += 1 # count the number of zeroes encountered
        else:
            temp.append(nums[i])
    print('Initial list:', nums)
    nums = temp + [0] * n # make a copy temp to preserve the order of the non-zeroes
    print('Modified list:', nums)