# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        low = 0
        high = len(nodes) - 1
        while low < high:
            nodes[low].next = nodes[high]
            low += 1
            if low >= high:
                break
            nodes[high].next = nodes[low]
            high -= 1
        nodes[low].next = None