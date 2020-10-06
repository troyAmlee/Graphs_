# from graph import Graph
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]



def earliest_ancestor(ancestors, starting_node):
    stack = []
    stack.append(starting_node)
    visited = []

    while(len(stack) > 0):
        deq = stack.pop()

        if(deq not in visited):
            visited.append(deq)

            for i in ancestors:
                if(i[1] == deq):
                    stack.append(i[0])
    if(visited[-1] == starting_node):
        return -1
    else:
        return visited[-1]

print(earliest_ancestor(test_ancestors, 1))
print(earliest_ancestor(test_ancestors, 2))
print(earliest_ancestor(test_ancestors, 3))
print(earliest_ancestor(test_ancestors, 4))
print(earliest_ancestor(test_ancestors, 5))
print(earliest_ancestor(test_ancestors, 6))
print(earliest_ancestor(test_ancestors, 7))
print(earliest_ancestor(test_ancestors, 8))
print(earliest_ancestor(test_ancestors, 9))
print(earliest_ancestor(test_ancestors, 10))
print(earliest_ancestor(test_ancestors, 11))
