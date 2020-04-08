# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def middleNode(head):
#         length = 0
#         start = head
#         while start:
#             length += 1
#             start = start.next
#         middle = length//2
#         count = 0
#         start = head
#         while count < middle:
#             start = start.next
#             count += 1
#         return start

# This works but there's a clever way to do this!

'''
We have two pointers traversing the linked list in different speeds. Two pointers, slow and fast
slow pointer moves one node at a time
fast pointer moves two nodes at a time
1 -> 2 -> 3 -> 4 -> 5
slow and fast are at 1 initially
slow moves to 2, fast moves to 3
slow moves to 3, fast moves to 5

At this point, fast has reached the end of the linked list.
If you have noticed, slow is at the middle of the linked list because it was moving at half of fast's speed


1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
s = f = 1
-- s = 2, f = 3
-- s = 3, f = 5
-- s = 4, f = 7
-- s = 5, f = 8

At this point, fast has reached the end of the linked list.
And slow has reached the middle of ll, so -- that does the trick.
'''


def solution(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Solution in one pass, it can't get better than that!
