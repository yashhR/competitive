# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(head):
        length = 0
        start = head
        while start:
            length += 1
            start = start.next
        middle = length//2
        count = 0
        start = head
        while count < middle:
            start = start.next
            count += 1
        return start