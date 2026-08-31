# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head):
        
        prev = head
        curr = head.next
        fut = head.next.next

        indices = []
        index = 1

        while fut:

            if ((prev.val < curr.val > fut.val) or
                (prev.val > curr.val < fut.val)):

                indices.append(index)

            prev = curr
            curr = fut
            fut = fut.next
            index += 1

        if len(indices) < 2:
            return [-1, -1]

        maxD = indices[-1] - indices[0]

        minD = float("inf")

        for i in range(1, len(indices)):
            minD = min(
                minD,
                indices[i] - indices[i - 1]
            )

        return [minD, maxD]