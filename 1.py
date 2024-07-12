class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a = ListNode(1, ListNode(2, ListNode(3, None)))
b = a.next
b.next.next = ListNode(322, None)
while a:
    print(a.val, id(a), id(b))
    a = a.next
