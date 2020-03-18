class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    def get_num(head):
        num = ''
        temp = head
        while temp.next is not None:
            num += str(temp.val)
            temp = temp.next
        num += str(temp.val)
        num = num[::-1]
        return int(num)

    num1 = get_num(l1)
    num2 = get_num(l2)
    retval = num1 + num2
    retval = str(retval)[::-1]
    one = ListNode(int(retval[0]))
    rettemp = one
    for idx in range(1, len(retval)):
        rettemp.next = ListNode(int(retval[idx]))
        rettemp = rettemp.next
    return one


k1 = ListNode(2)
k1.next = ListNode(4)
k1.next.next = ListNode(3)

k2 = ListNode(5)
k2.next = ListNode(6)
k2.next.next = ListNode(4)

ans = addTwoNumbers(k1, k2)

anstemp = ans

while anstemp.next is not None:
    print(anstemp.val, end="")
    anstemp = anstemp.next
print(anstemp.val)

