from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head is None or head.next is None:
            return None
        
        # create a pointer node to traverse linked list in place of the original
        count = head
        num_node = 0
        while count:
            count = count.next
            num_node += 1 # we are counting the max index of this 0-based indexing linked list

        # The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, 
        # where ⌊x⌋ denotes the largest integer less than or equal to x.
        # example: 7 nodes, middle node is the 3th node from the start.
        mid = (num_node // 2)

        count = head

        while mid > 1:
            mid -= 1
            count = count.next

        count.next = count.next.next

        return head
    
     # Method deletes middle node
     # Optimized version: https://www.prepbytes.com/blog/linked-list/delete-middle-of-linked-list/#:~:text=The%20naive%20approach%20to%20deleting,node%20of%20the%20linked%20list.&text=The%20algorithm%20for%20the%20above,head%20is%20NULL%2C%20return%20NULL.
    def deleteMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases
        if (head is None or
            head.next is None):
            return
        
        # Floyd's Tortoise and Hare algorithm to implement a pair of pointers
        # fast traverses twice as fast as the slow -> when slow is at the middle of the list, fast should be at the end of list (either fast == Null, or fast.next == Null)

        
        # Initialize slow and fast pointers
        slow_ptr = head
        fast_ptr = head

        # Find the middle and previous of middle
        prev = None # To store previous of slow pointer

        while (fast_ptr is not None and fast_ptr.next is not None): # check fast if reaches the end of linkedlist, slow should always be at the middle
            fast_ptr = fast_ptr.next.next
            prev = slow_ptr
            slow_ptr = slow_ptr.next
        # Delete the middle node
        prev.next = slow_ptr.next
        
        return head