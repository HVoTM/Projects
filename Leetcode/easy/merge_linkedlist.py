from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # init a ListNode to return value in function
        mergedlist = ListNode(val=0, next=None)
        # create a temporary value which points to the empty linkedlist we initialized
        # NOTE: we use this temp to ListNode - a mutable object. So any update on temp would also change the pointed value
        # As for linkedlist, we need to keep the head for the return value of this function
        # which makes for the need of a temp value
        # NOTE: moreover, temp value which is a pointer to an integer var would not behave the same
        # since integer is an immutable value - which is not inherent to change
        temp = mergedlist

        # loop that will check if two linked lists are still being traversed
        while (list1 != None) & (list2 != None):
            # compare the two current nodes' values
            if list1.val <= list2.val:
                temp.next = list1   # assign the current satisfied node in the two lists to the next node of mergedlist
                list1 = list1.next # move on to the next node
            else: # same idea
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        # if the end of one list is reached, the remaining nodes of the other linked list is assigned to the next node 
        # of the current node (current node will point to next one and on towards, no need for loop)
        if list1 == None:
            temp.next = list2
        if list2 == None:
            temp.next = list1
        
        # for now, the head is still retaining the initial value 0 we init before
        # we can delete that node and make the next node the head, but that would take more space and runtime
        # just return the next node from the head node!
        return mergedlist.next

