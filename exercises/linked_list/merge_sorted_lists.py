"""
Merge sorted lists: EPI 7.1
"""


class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def merge(l1, l2):
    prehead = current = ListNode(None)

    while l1 and l2:
        if l1.val <= l2.val:
            current.next, l1 = l1, l1.next
        else:
            current.next, l2 = l2, l2.next
        current = current.next

    current.next = l1 or l2

    return prehead.next
