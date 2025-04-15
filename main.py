import os
os.system("cls")  

import math

graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'D': 4, 'E': 1},
    'C': {'A': 5, ' F': 3},
    'D': {'B': 4, 'G': 6},
    'E': {'B': 1, 'H': 7},
    'F': {'C': 3, 'I': 2},
    'G': {'D': 6, 'J': 4},
    'H': {'E': 7, 'K': 5},
    'I': {'F': 2, 'L': 3},
    'J': {'G': 4, 'M': 6},
    'K': {'H': 5, 'N': 2},
    'L': {'I': 3, 'O': 4},
    'M': {'J': 6, 'P': 1},
    'N': {'K': 2, 'Q': 3},
    'O': {'L': 4, 'R': 2},
    'P': {'M': 1, 'S': 5},
    'Q': {'N': 3, 'T': 6},
    'R': {'O': 2},
    'S': {'P': 5},
    'T': {'Q': 6}
}

start = 'C'
distances = {node: math.inf for node in graph}
visited = []

distances[start] = 0
print(distances)


def dijikstra():
    unvisited = {node: distance for node, distance in distances.items() if node not in visited}
    currNode = min(unvisited, key=unvisited.get)
    print (currNode)

    for neighbor, edgeValue in graph[currNode].items():
        if neighbor not in visited:
            tempDistance = distances[currNode]+ edgeValue
            if tempDistance< distances[neighbor]:
                 distances[neighbor] = tempDistance
    visited.append(currNode)
    if(len(visited)<len(graph)):
        dijikstra()             
    else:
        print("Final distances", distances)
dijikstra()
