import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User({repr(self.name)})"

class SocialGraph:
    def __init__(self):
        self.reset()

    def addFriendship(self, userID, friendID): # Add Edge
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name): # Add Node/Vertex
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def reset(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}
    
    def populateGraph(self, numUsers, avgFriendships): # Creates a randomly generated grid
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.reset()
        # !!!! IMPLEMENT ME
        for i in range(numUsers):
            self.addUser(f"User {i}")
        # Add users
        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.lastID + 1):
                possible_friendships.append((user_id, friend_id))
        random.shuffle(possible_friendships)

        for i in range(numUsers * avgFriendships // 2):
            friendships = possible_friendships[i]
            self.addFriendship(friendships[0], friendships[1])
        # Create friendships

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
                for i in self.friendships[deq]:
                    q.push(i)
        return visited 

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
                for i in self.friendships[deq]:
                    q.enqueue(i)
        return visited 

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
                for i in self.friendships[last]:
                    deq.append(i)
                    c = deq.copy()
                    q.enqueue(c)
                    deq.pop()
                # COPY THE PATH
                # APPEND THE NEIGHOR TO THE BACK
        return None

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # get all social paths from the specified user

        q = Queue()

        if(userID in self.friendships):
            
            q.queue = self.bft(userID)

            for i in q.queue:
                visited[i] = self.bfs(userID, i)

            return visited

    def percent_in_network(self, id):
        return f"{(len(self.getAllSocialPaths(id))/len(self.users)) * 100}%"

    def avg_degree(self, id):
        count = 0
        connections = self.getAllSocialPaths(id)
        num_of_connections = len(connections)
        for i in connections:
            try:
                count += (len(connections[i]) - 1)
            except:
                pass
        return (f"Average degree: {count/num_of_connections}")

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    print(sg.users)
    print("--------------------------------")
    print(sg.friendships)
    print("--------------------------------")
    connections = sg.getAllSocialPaths(1)
    print(connections)
    print("--------------------------------")
    print("Percent of other users in extended social network")
    print(sg.percent_in_network(1))
    print("--------------------------------")
    print(sg.avg_degree(1))