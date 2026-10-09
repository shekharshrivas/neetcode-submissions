# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # len = 0
        # temp = head
        # while temp:
        #     len += 1
        #     temp = temp.next
        # if len - n == 0:
        #     return head.next
        # removeIndex = len - n - 1
        # temp = head
        # for i in range(removeIndex):
        #     temp = temp.next
        # temp.next = temp.next.next
        # return head

        fast = head
        for i in range(n):
            fast = fast.next
        slow = head
        if fast == None:
            return head.next
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        delnode = slow.next
        slow.next = slow.next.next
        delnode.next = None
        return head
