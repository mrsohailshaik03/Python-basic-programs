
# Aim: To implement DFS and BFS
# Algorithm:
# DFS Algorithm
# The DSF algorithm follows as:
# 1.	We will start by putting any one of the graph's vertex on top of the stack.
# 2.	After that take the top item of the stack and add it to the visited list of the vertex.
# 3.	Next, create a list of that adjacent node of the vertex. Add the ones which aren't in the visited list of vertexes to the top of the stack.
# 4.	Lastly, keep repeating steps 2 and 3 until the stack is empty.
# BFS Algorithm
# The BSF algorithm follows as:
# 1.	 Start by putting any one of the graph’s vertices at the back of the queue.
# 2.	 Now take the front item of the queue and add it to the visited list.
# 3.	 Create a list of that vertex's adjacent nodes. Add those which are not within the visited list to the rear of the queue.
# 4.	 Keep continuing steps two and three till the queue is empty.
# Program: -
# Breadth-First Search (BFS)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m, end="  ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Flowing in BFS")
bfs(visited, graph, 'A')
print('\n')

# Depth-First Search (DFS)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end="  ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Flowing in DFS")
dfs(visited, graph, 'A')
print('\n')







