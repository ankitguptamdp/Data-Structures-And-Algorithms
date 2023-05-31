# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        # Find the middle node (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse the second half of the linked list
        previous = None        
        while slow:
            temp = slow.next
            slow.next = previous
            previous = slow
            slow = temp

        # Checking whether the linked list is palindrome or not
        left = head
        right = previous
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True