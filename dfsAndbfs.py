import collections

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex), end=" ")

        # If not visited, mark it as visited, and enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
               
def dfs(visited, graph, node):  #function for dfs
    if node not in visited:
        print (node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
           

graph = {'S': ['A', 'B', 'C'], 'A': ['S','D'], 'B': ['S','G'], 'C': ['S','G'], 'D': ['A','G'], 'G': ['D', 'B', 'C'] }
print("BFS Graph 1: ")
bfs(graph, 'S')

print()

graph = {1:[2, 3], 2: [1, 4, 5], 3: [1, 6, 7], 4: [2], 5: [2], 6: [3], 7: [3]}
print("BFS Graph 2: ")
bfs(graph, 1)

print()

visited = set()
print("DFS Graph 2: ")
dfs(visited, graph, 1)