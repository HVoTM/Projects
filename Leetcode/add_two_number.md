```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Linkedlist key to return
        key = None
        # works like a reference node, for interchanging and updating value for every iterations
        temp = None
        # carry value for next set
        carry = 0
        # Loop for the 2 lists and do the summation
        while l1 is not None or l2 is not None:
            # At the start of each iteration, we should add carry from the last iteration
            sum_value = carry
            # Since the lengths of the lists may be unequal, we are checking if the
            # current node is null for one of the lists
            if l1 is not None:
                sum_value += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_value += l2.val
                l2 = l2.next
            # At this point, we will add the total sum_value % 10 to the new node
            # in the resultant list
            node = ListNode(sum_value % 10)
            # Carry to be added in the next iteration
            carry = sum_value // 10
            # If this is the first node or head
            if temp is None:
                temp = key = node
            # for any other node
            else:
                temp.next = node
                temp = temp.next
        # After the last iteration, we will check if there is carry left
        # If it's left then we will create a new node and add it
        if carry > 0:
            temp.next = ListNode(carry)
        return key
```