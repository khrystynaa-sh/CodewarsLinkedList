from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if node is None:
        raise Exception

    ind = 0
    while node:
        if ind == index:
            return node
        node = node.next
        ind += 1
        
    raise Exception
  
