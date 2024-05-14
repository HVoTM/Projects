from typing import List

class Solution:
    # My solution
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        temp1 = []
        temp2 = []
        for i in nums1:
            if i not in nums2 and i not in temp1:
                temp1.append(i)
        for j in nums2 :
            if j not in nums1 and j not in temp2:
                temp2.append(j)
        return [temp1, temp2]
    
    # A better solution
    # Python Set data structure: https://docs.python.org/3/tutorial/datastructures.html#sets
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2) # we modify the arrays into sets 
        # Because set items are unordered, unchangeable, and DO NOT ALLOW DUPLICATE VALUES  
        # as we are considering cases where there are duplicate values in a array, the algorithm may accidentally add more than necessary
        return [list(set1 - set2), list(set2 - set1)]
