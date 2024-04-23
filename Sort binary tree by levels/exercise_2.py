def tree_by_levels(node):
    result = []
    queue = [node]
    count = 0

    while len(queue) > count:
        current_n = queue[count]
        count += 1
        
        if current_n is None:
            break
        
        result.append(current_n.value)

        if current_n.left:
            queue.append(current_n.left)
        if current_n.right:
            queue.append(current_n.right)

    return result