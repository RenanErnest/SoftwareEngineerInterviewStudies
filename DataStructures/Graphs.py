from LinkedLists import LinkedList
from collections import deque

'''
Deegre of a vertex: number of edges coming in or out of the vertex
Adjacency: two vertices are adjacent if there is an edge between them
Undirected graph: max(edges) = n*(n-1)/2 excluding self loops, if not (n^2)/2
Directed graph: max(edges) = n*(n-1) excluding self loops, if not n^2
Directed graph adjacency matrix: rows are sources and columns are destinations

Operation               Adjacency List  Adjacency Matrix
Add Vertex	                O(1)	        O(V^2)
Remove Vertex	            O(V+E)	        O(V^2)
Add Edge	                O(1)	        O(1)
Remove Edge	                O(E)	        O(1)
Search	                    O(V)	        O(1)
Breadth First Search(BFS)	O(V+E)	        O(V^2)
Depth First Search(DFS)	    O(V+E)      	O(V^2)

All the acyclic graphs can be bi-partite, but in the case of cyclic graphs, they must contain an even number of vertices.
'''


class Graph:
    def __init__(self, number_of_vertices):
        self.number_of_vertices = number_of_vertices
        self.adjacency_list = [LinkedList() for vertex in range(number_of_vertices)]

    def add_edge(self, source, destination):
        if source >= 0 and source < self.number_of_vertices and destination >= 0 and destination < self.number_of_vertices:
            self.adjacency_list[source].insert(destination)

    def print(self):
        print('Number of vertices:', self.number_of_vertices)
        for v in range(self.number_of_vertices):
            print(v,': ',sep='', end='')
            self.adjacency_list[v].print()

    def bfs_traversal(self, source):
        def bfs(source, visited):
            result = ''
            queue = deque([source])
            visited[source] = True
            while queue:
                vertex = queue.popleft()
                result += str(vertex)
                adjacent_vertex = self.adjacency_list[vertex].get_head()
                while adjacent_vertex:
                    if not visited[adjacent_vertex.val]:
                        visited[adjacent_vertex.val] = True
                        queue.append(adjacent_vertex.val)
                    adjacent_vertex = adjacent_vertex.next
            return result

        if source < 0 or source >= self.number_of_vertices:
            return ''

        result = ''
        visited = [False] * self.number_of_vertices

        result += bfs(source, visited)
        for vertex in range(self.number_of_vertices):
            if not visited[vertex]:
                result += bfs(vertex, visited)

        return result

    def dfs_traversal(self, source):
        def dfs(source, visited):
            result = ''
            stack = [source]
            visited[source] = True
            while stack:
                vertex = stack.pop()
                result += str(vertex)
                adjacents = self.adjacency_list[vertex]
                adjacent_vertex = adjacents.get_head()
                while adjacent_vertex:
                    if not visited[adjacent_vertex.val]:
                        visited[adjacent_vertex.val] = True
                        stack.append(adjacent_vertex.val)
                    adjacent_vertex = adjacent_vertex.next
            return result

        if source < 0 or source >= self.number_of_vertices:
            return ''
        result = ''
        visited = [False for vertex in range(self.number_of_vertices)]
        result += dfs(source, visited)

        for vertex in range(self.number_of_vertices):
            if not visited[vertex]:
                result += dfs(vertex, visited)

        return result


class GraphMatrix:
    def __init__(self, number_of_vertices):
        self.number_of_vertices = number_of_vertices
        self.adjacency_matrix = [[0 for column in range(number_of_vertices)] for row in range(number_of_vertices)]

    def add_edge(self, source, destination):
        if 0 <= source < self.number_of_vertices and 0 <= destination < self.number_of_vertices:
            self.adjacency_matrix[source][destination] = 1

    def print(self):
        for row in self.adjacency_matrix:
            print(row)

    def bfs_traversal(self, source):
        def bfs(source, visited):
            result = ''
            queue = deque([source])
            visited[source] = True
            while queue:
                vertex = queue.popleft()
                result += str(vertex)
                for adjacent_vertex in range(len(self.adjacency_matrix[vertex])):
                    if self.adjacency_matrix[vertex][adjacent_vertex] == 1: # enqueue
                        if not visited[adjacent_vertex]:
                            visited[adjacent_vertex] = True
                            queue.append(adjacent_vertex)
            return result

        if source < 0 or source >= self.number_of_vertices:
            return ''

        result = ''
        visited = [False] * self.number_of_vertices

        result += bfs(source, visited)
        for vertex in range(self.number_of_vertices):
            if not visited[vertex]:
                result += bfs(vertex,visited)

        return result

    def dfs_traversal(self, source):
        def dfs(source, visited):
            result = ''
            stack = [source]
            visited[source] = True

            while stack:
                vertex = stack.pop()
                result += str(vertex)
                for adjacent_vertex in range(len(self.adjacency_matrix[vertex])):
                    if self.adjacency_matrix[vertex][adjacent_vertex] == 1:
                        if not visited[adjacent_vertex]:
                            visited[adjacent_vertex] = True
                            stack.append(adjacent_vertex)

            return result

        if source < 0 or source >= self.number_of_vertices:
            return ''

        result = ''
        visited = [False for vertex in range(self.number_of_vertices)]
        result += dfs(source, visited)

        for vertex in range(self.number_of_vertices):
            if not visited[vertex]:
                result += dfs(vertex, visited)

        return result

'''
Time complexity: O(v+e)
Space complexity: O(v)
'''
def detect_cycle(g):
    if not g:
        return False

    visited = set()
    for vertex in range(g.number_of_vertices):
        if vertex not in visited:
            if detect_cycle_dfs_traversal(g, vertex, visited):
                return True

    return False


def detect_cycle_dfs_traversal(graph, source, visited):
    stack = [source]
    visited.add(source)

    while stack:
        vertex = stack.pop()
        adjacent_vertex = graph.adjacency_list[vertex].get_head()
        while adjacent_vertex:
            if adjacent_vertex.val in visited:
                return True
            visited.add(adjacent_vertex.val)
            stack.append(adjacent_vertex.val)
            adjacent_vertex = adjacent_vertex.next

    return False

'''
Time complexity: O(v*(v+e))
Space complexity: O(v)

Could be done in O(v+e) if we do an entire traversal and store the last vertex used (the one that completed the visited set), 
that could potentially be the mother vertex. After that we just need to double check if this last vertex can reach every other
vertex, if so, return it because it is a mother vertex, otherwise return an invalid value
'''
def find_mother_vertex(g):
    global_visited = set()
    for vertex in range(g.number_of_vertices):
        if vertex not in global_visited:
            if check_mother_vertex_bfs(g,vertex,global_visited):
                return vertex
    return -1


def check_mother_vertex_bfs(graph, source, global_visited):
    queue = deque([source])
    local_visited = set()
    local_visited.add(source)
    global_visited.add(source)

    while queue:
        vertex = queue.popleft()
        adjacent_vertex = graph.adjacency_list[vertex].get_head()
        while adjacent_vertex:
            if adjacent_vertex.val not in local_visited:
                local_visited.add(adjacent_vertex.val)
                global_visited.add(adjacent_vertex.val)
                queue.append(adjacent_vertex.val)
            adjacent_vertex = adjacent_vertex.next

    return graph.number_of_vertices == len(local_visited)

'''
Time complexity: O(v+e)
Space complexity: O(v)
'''
def find_mother_vertex_efficient(graph):
    if not graph or graph.number_of_vertices <= 0:
        return -1

    visited = set()
    last_traversed_vertex = -1
    for source in range(graph.number_of_vertices):
        if source not in visited:
            check_mother_vertex_efficient_bfs(graph, source, visited)
            last_traversed_vertex = source

    visited = set()
    if check_mother_vertex_efficient_bfs(graph, last_traversed_vertex, visited):
        return last_traversed_vertex
    return -1


def check_mother_vertex_efficient_bfs(graph, source, visited):
    queue = deque([source])
    visited.add(source)

    while queue:
        vertex = queue.popleft()
        adjacent_vertex = graph.adjacency_list[vertex].get_head()
        while adjacent_vertex:
            if adjacent_vertex.val not in visited:
                visited.add(adjacent_vertex.val)
                queue.append(adjacent_vertex.val)
            adjacent_vertex = adjacent_vertex.next

    return graph.number_of_vertices == len(visited)


'''
Return the number of edges of an undirected graph
Time complexity: O(v+e)
Space complexity: O(1)
'''
def num_edges(graph):
    number_of_edges = 0
    for vertex in range(graph.number_of_vertices):
        adjacent_vertex = graph.adjacency_list[vertex].get_head()
        while adjacent_vertex:
            number_of_edges += 1
            adjacent_vertex = adjacent_vertex.next

    return number_of_edges // 2


'''
Time complexity: O(v+e)
Space complexity: O(v)
'''
def check_path(graph, source, destination):
    if source < 0 or source >= graph.number_of_vertices or destination < 0 or destination >= graph.number_of_vertices:
        return False
    visited = {source}
    queue = deque([source])

    while queue:
        vertex = queue.popleft()
        if vertex == destination:
            return True

        adjacent_vertex = graph.adjacency_list[vertex].get_head()
        while adjacent_vertex:
            if adjacent_vertex.val not in visited:
                visited.add(adjacent_vertex.val)
                queue.append(adjacent_vertex.val)
            adjacent_vertex = adjacent_vertex.next

    return False


'''
Find if an undirected graph is a tree
Time complexity: O(v+e)
Space complexity: O(2v) = O(v)
'''
def is_tree(g):
    # choose a random start, 0 for example
    visited = {0}
    queue = deque([(0, -1)])

    while queue:
        vertex, parent = queue.popleft()

        adjacent_vertex = g.adjacency_list[vertex].get_head()
        while adjacent_vertex:
            if adjacent_vertex.val in visited and adjacent_vertex.val != parent:
                return False
            visited.add(adjacent_vertex.val)
            queue.append((adjacent_vertex.val, vertex))
            adjacent_vertex = adjacent_vertex.next

    return len(visited) == g.number_of_vertices


'''
Return the number of edges for the shortest path

It could be done in a BFS level traversal
Time complexity: O(v+e)
Space complexity: O(v)
'''
def find_shortest_path(graph, source, destination):
    visited = set([source])
    queue = deque([source])
    level = 0

    while queue:
        size = len(queue)
        for vertex_in_the_level in range(size):
            vertex = queue.popleft()
            if vertex == destination:
                return level

            adjcent_vertex = graph.adjacency_list[vertex].get_head()
            while adjcent_vertex:
                if adjcent_vertex.val not in visited:
                    visited.add(adjcent_vertex.val)
                    queue.append(adjcent_vertex.val)
                adjcent_vertex = adjcent_vertex.next
        level += 1
    return -1


'''
Time complexity: O(v) or O(min(v,e))
Space complexity: O(1)
'''
def remove_edge(graph, source, dest):
    # remove dest from the source's adjacency list
    head = graph.adjacency_list[source].get_head()
    if head and head.val == dest:
        graph.adjacency_list[source].head_node = head.next
        return graph

    prev = None
    curr_vertex = head
    while curr_vertex:
        if curr_vertex.val == dest:
            prev.next = curr_vertex.next
            return graph
        prev = curr_vertex
        curr_vertex = curr_vertex.next
    return graph


graph = Graph(5)
graph.add_edge(0,2)
graph.add_edge(0,3)
graph.add_edge(3,4)
graph.print()
print()
print(graph.bfs_traversal(0))
print(graph.dfs_traversal(0))
print(detect_cycle(graph))
print('isTree: ', is_tree(graph))
graph.add_edge(4,0)
print(detect_cycle(graph))
print(find_mother_vertex(graph))
print(find_mother_vertex_efficient(graph))
graph.add_edge(4,1)
print(find_mother_vertex(graph))
print(find_mother_vertex_efficient(graph))
graph.print()
print(check_path(graph, 0, 4))
print(check_path(graph, 2, 0))
print('isTree: ', is_tree(graph))
print(find_shortest_path(graph, 0, 4))
graph.add_edge(0,4)
print(find_shortest_path(graph, 0, 4))



print()
graph = GraphMatrix(5)
graph.add_edge(0,2)
graph.add_edge(0,3)
graph.add_edge(3,4)
graph.print()
print()
print(graph.bfs_traversal(0))
print(graph.dfs_traversal(0))