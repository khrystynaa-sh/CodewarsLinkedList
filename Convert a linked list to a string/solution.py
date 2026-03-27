def stringify(node):
    head = node
    text = ""
    while head:
        text += f"{head.data}" + " -> "
        head = head.next
    text += "None"
    return text
