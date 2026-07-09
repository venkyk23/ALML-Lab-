from collections import deque

# Define the social network graph
graph = {
    "Alice": ["Charlie", "David"],
    "Charlie": ["Alice", "Emma"],
    "David": ["Alice", "Emma", "Fred"],
    "Emma": ["Charlie", "David", "Bob"],
    "Fred": ["David", "Bob"],
    "Bob": ["Emma", "Fred"]
}

# BFS Implementation
def bfs(start, goal):
    visited = []
    queue = deque([[start]])  # queue stores paths
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node not in visited:
            visited.append(node)
            
            if node == goal:
                return path
            
            for neighbor in sorted(graph[node]):  # alphabetical order
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

# DFS Implementation
def dfs(start, goal):
    visited = []
    stack = [[start]]  # stack stores paths
    
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node not in visited:
            visited.append(node)
            
            if node == goal:
                return path
            
            # push neighbors in reverse alphabetical order (so stack pops correctly)
            for neighbor in sorted(graph[node], reverse=True):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

# Run simulations
print("BFS Path from Alice to Bob:", bfs("Alice", "Bob"))
print("DFS Path from Alice to Bob:", dfs("Alice", "Bob"))
