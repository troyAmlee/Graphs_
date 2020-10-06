"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Nonexistent vertex/node")
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = list()
        while(q.size() > 0):
            deq = q.dequeue()
            if(deq not in visited):
                visited.append(deq)
                for i in self.vertices[deq]:
                    q.enqueue(i)
        print(visited)
        return visited            
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        q = Stack()
        q.push(starting_vertex)
        visited = list()
        while(q.size() > 0):
            deq = q.pop()
            if(deq not in visited):
                visited.append(deq)
                for i in self.vertices[deq]:
                    q.push(i)
        print(visited)
        return visited 
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if(type(starting_vertex) == type(0)):
            stack = [[starting_vertex], []]
            
        elif(type(starting_vertex) == type(list())):
            stack = starting_vertex
        if(len(stack[0]) > 0):
            deq = stack[0].pop()
            if(deq not in stack[1]):
                print(deq)
                stack[1].append(deq)
                for i in self.vertices[deq]:
                    stack[0].append(i)
                return self.dft_recursive(stack)
            return self.dft_recursive(stack)
        print(starting_vertex[1])
        return starting_vertex[1]
        

            
    def bfs(self, starting_vertex, destination_vertex):
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
                # Create a Set to store visited vertices
        visited = set()
                # While the queue is not empty...
        while(q.size() > 0):
            # Dequeue the first PATH
            deq = q.dequeue()
            # Grab the last vertex from the PATH
            last = deq[-1]
            # If that vertex has not been visited...
            if(last not in visited):
                # CHECK IF IT'S THE TARGET
                if(last == destination_vertex):
                # IF SO, RETURN PATH
                    return deq
                # Mark it as visited...
                visited.add(last)
                # Then add A PATH TO its neighbors to the back of the queue
                for i in self.vertices[last]:
                    deq.append(i)
                    c = deq.copy()
                    q.enqueue(c)
                    deq.pop()
                # COPY THE PATH
                # APPEND THE NEIGHOR TO THE BACK

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
                # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Stack()
        q.push([starting_vertex])
                # Create a Set to store visited vertices
        visited = set()
                # While the queue is not empty...
        while(q.size() > 0):
            # Dequeue the first PATH
            deq = q.pop()
            # Grab the last vertex from the PATH
            last = deq[-1]
            # If that vertex has not been visited...
            if(last not in visited):
                # CHECK IF IT'S THE TARGET
                if(last == destination_vertex):
                # IF SO, RETURN PATH
                    return deq
                # Mark it as visited...
                visited.add(last)
                # Then add A PATH TO its neighbors to the back of the queue
                for i in self.vertices[last]:
                    deq.append(i)
                    c = deq.copy()
                    q.push(c)
                    deq.pop()
                # COPY THE PATH
                # APPEND THE NEIGHOR TO THE BACK

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if(type(starting_vertex) == type(0)):
            stack = [[[starting_vertex]], []]
            
        elif(type(starting_vertex) == type(list())):
            stack = starting_vertex

        if(len(stack[0]) > 0):
            deq = stack[0].pop()
            last = deq[-1]
            if(last not in stack[1]):
                
                if(last == destination_vertex):
                    return deq

                stack[1].append(last) # adding to visited (stack[1])

                for i in self.vertices[last]:
                    deq.append(i)
                    c = deq.copy()
                    deq.pop()
                    stack[0].append(c)
                return self.dfs_recursive(stack, destination_vertex)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("dft")
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("bft")
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("dft recursive")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("bfs")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("dfs")
    print(graph.dfs(1, 6))
    print("dfs recursive")
    print(graph.dfs_recursive(1, 6))