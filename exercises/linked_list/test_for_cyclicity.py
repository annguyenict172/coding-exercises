"""
Check for cyclicity: EPI 7.3
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def get_cycle_len(node_in_cycle):
    anchor = node_in_cycle
    step = 1
    while True:
        node_in_cycle = node_in_cycle.next
        if node_in_cycle == anchor:
            return step
        else:
            step += 1


def get_start_node_in_cycle(L, cycle_len):
    head = tail = L
    delay = cycle_len
    while True:
        tail = tail.next
        if delay == 0:
            head = head.next
        else:
            delay -= 1

        if head == tail:
            return head


def test_for_cyclicity(L):
    slow = fast = L
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if fast == slow:
            cycle_len = get_cycle_len(slow)
            begin_of_cycle = get_start_node_in_cycle(L, cycle_len)
            return begin_of_cycle

    return False


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = b

print(test_for_cyclicity(a))
