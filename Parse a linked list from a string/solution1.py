from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == 'null':
        return None
    
    nodes = list_repr.split(" -> ")
    nodes = nodes[:-1]
    nodes = [int(i) for i in nodes]
    next_node = None
    for node in reversed(nodes):
        new_node = Node(node, next_node)
        next_node = new_node
    return next_node
