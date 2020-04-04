def delete_duplicates(head):
    haha = head
    while head:
        print(head.val)
        if head.next and head.next.val == head.val:
            current = head
            while current.next and current.next.val == current.val:
                current = current.next
            head.next = current.next
            head = head.next
        else:
            head = head.next
    return haha


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


head = ListNode(2)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(2)
head.next.next.next.next.next = ListNode(2)


ans = delete_duplicates(head)
anstemp = ans

while anstemp:
    print(f"{anstemp.val} -> ", end="")
    anstemp = anstemp.next

# This solution does better than 70% of all python solutions
