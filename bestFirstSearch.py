from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    queue = PriorityQueue()
    queue.put((heuristic[start], start))  # Enqueue the start node with its heuristic value
    visited = set()  # Set to keep track of visited nodes
    came_from = {}  # Dictionary to store the parent of each node

    while not queue.empty():
        _, current = queue.get()  # Dequeue the node with the lowest priority

        if current == goal:
            # Reconstruct and print the path
            path = reconstruct_path(came_from, start, goal)
            print("Path:", " -> ".join(path))
            return True  # Solution found

        visited.add(current)  # Mark the current node as visited

        for neighbor in graph[current]:
            if neighbor not in visited:
                priority = heuristic[neighbor]  # Calculate the priority (heuristic value)
                queue.put((priority, neighbor))  # Enqueue the neighbor with its priority
                came_from[neighbor] = current  # Set the parent of the neighbor

    return False  

def reconstruct_path(came_from, start, goal):
    path = [goal]
    current = goal
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

# Example graph represented as an adjacency list
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'D': ['F'],
    'F': ['I', 'G'],
    'E': ['H']
}

# Heuristic values for each node
heuristic = {
    'A': 12,
    'B': 11,
    'C': 7,
    'D': 3,
    'E': 8,
    'F': 2,
    'G': 0,
    'I':9,
    'H':4,
    'S':13
}

start_node = 'S'
goal_node = 'G'

result = best_first_search(graph, start_node, goal_node, heuristic)

if result:
    print("Goal reached!")
else:
    print("No solution found.")