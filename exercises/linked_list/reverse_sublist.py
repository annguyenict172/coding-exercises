class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def traverse(head):
    cur = head
    while cur is not None:
        print(cur.val)
        cur = cur.next


def reverse_sublist(L, start, finish):
    dummy_head = sublist_head = Node(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next

        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next


elem1 = Node(1)
elem2 = Node(2)
elem3 = Node(3)
elem4 = Node(4)
elem5 = Node(5)
elem6 = Node(6)

elem1.next = elem2
elem2.next = elem3
elem3.next = elem4
elem4.next = elem5
elem5.next = elem6

new = reverse_sublist(elem1, 1, 6)
traverse(new)
