class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

# Pre-order traversal
def pre_order(node):
    if node is None:
        return []

    result = []
    stack = [node]
    
    while stack:
        current = stack.pop(0)
        result.append(current.data)
        
        if current.right is not None:
            stack.insert(0, current.right)

        if current.left is not None:
            stack.insert(0, current.left)
    
    return result
 
# In-order traversal
def in_order(node):
    if node is None:
        return []

    result = []
    stack = []
    current = node

    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.data)
        current = current.right

    return result

# Post-order traversal
def post_order(node):
    if node is None:
        return []

    result = []
    stack = []
    current = node

    while stack or current:
        while current:
            if current.right:
                stack.append(current.right)
            stack.append(current)
            current = current.left

        current = stack.pop()

        if current.right and stack and stack[-1] == current.right:
            stack.pop()
            stack.append(current)
            current = current.right
        else:
            result.append(current.data)
            current = None

    return result
