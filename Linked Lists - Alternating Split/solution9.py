class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise Exception

    first_head = head
    second_head = head.next
    current_first = first_head
    current_second = second_head
    while current_first and current_second:
        current_first.next = current_second.next
        current_first = current_first.next
        if current_first:
            current_second.next = current_first.next
        else:
            current_second.next = None
        current_second = current_second.next
    return Context(first_head, second_head)
