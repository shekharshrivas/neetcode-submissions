# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # nodes = []
        # current = head
        # while current:
        #     nodes.append(current)
        #     current = current.next
        # low = 0
        # high = len(nodes) - 1
        # while low < high:
        #     nodes[low].next = nodes[high]
        #     low += 1
        #     if low >= high:
        #         break
        #     nodes[high].next = nodes[low]
        #     high -= 1
        # nodes[low].next = None

        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2