romania_graph = {
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Zerind": {"Oradea": 71, "Arad": 75},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Drobeta": 75},
    "Drobeta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
    "Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
    "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90},
    "Giurgiu": {"Bucharest": 90},
}

def dfs_iterative(root, goal):
    stack = [root]
    visited = set()
    
    while stack:
        node = stack.pop()
        
        if node == goal:
            print(node, end=" ")
            return True
        
        if node not in visited:
            visited.add(node)
            print(node, end=" -> ")
            
            # Push unvisited neighbors onto the stack
            for neighbor in romania_graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                
    return False
    
print("Iterative DFS: ")
dfs_iterative("Arad", 'Bucharest')
