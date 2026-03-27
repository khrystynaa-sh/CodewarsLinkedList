from preloaded import Node

def swap_pairs(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    current = head
    while current and current.next:
        first = current
        second = current.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
        current = first.next
    return dummy.next
