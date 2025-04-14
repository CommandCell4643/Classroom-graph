import os
os.system("clear")
import math

my_list = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start = 'A'
distances = {node: math.inf for node in my_list}
visitedNodes = []
distances[start] = 0
print(distances)

def dijikstra():
currNode = min(distances.values())       