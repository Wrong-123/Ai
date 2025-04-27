from collections import deque

def bfs(graph, start):
    visited = set()           # To keep track of visited nodes
    queue = deque([start])    # Initialize queue with the starting node

    print("BFS Traversal:")
    while queue:
        node = queue.popleft()  # Remove the first element from the queue
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start, end=' ')
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Example graph using dictionary (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS
bfs(graph, 'A')

print("\nDFS Traversal:")
# Run DFS
dfs(graph, 'A')
