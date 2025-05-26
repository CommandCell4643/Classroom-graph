import os
os.system("clear")  

import math

mainGraph = {
    'A': {'B': 2, 'C': 3, 'D': 4, 'E': 5},
    'B': {'A': 2, 'C': 1, 'F': 3, 'G': 6},
    'C': {'A': 3, 'B': 1, 'H': 2, 'I': 4},
    'D': {'A': 4, 'E': 2, 'J': 5, 'K': 3},
    'E': {'A': 5, 'D': 2, 'L': 4, 'M': 1},
    'F': {'B': 3, 'G': 2, 'N': 6, 'O': 5},
    'G': {'B': 6, 'F': 2, 'P': 3, 'Q': 4},
    'H': {'C': 2, 'I': 3, 'R': 5, 'S': 1},
    'I': {'C': 4, 'H': 3, 'T': 2, 'U': 6},
    'J': {'D': 5, 'K': 2, 'V': 3, 'W': 4},
    'K': {'D': 3, 'J': 2, 'X': 6, 'Y': 5},
    'L': {'E': 4, 'M': 3, 'Z': 1, 'N': 2},
    'M': {'E': 1, 'L': 3, 'O': 4, 'P': 2},
    'N': {'F': 6, 'L': 2, 'Q': 3, 'R': 5},
    'O': {'F': 5, 'M': 4, 'S': 2, 'V': 6},
    'P': {'G': 3, 'M': 2, 'U': 4, 'V': 1},
    'Q': {'G': 4, 'N': 3, 'W': 2, 'X': 1},
    'R': {'H': 5, 'N': 5, 'Y': 3, 'Z': 4},
    'S': {'H': 1, 'O': 2, 'X': 5, 'Y': 6},
    'T': {'I': 2, 'O': 6, 'Z': 3, 'V': 4},
    'U': {'I': 6, 'P': 4, 'W': 2, 'X': 3},
    'V': {'J': 3, 'P': 1, 'T': 4, 'Y': 2},
    'W': {'J': 4, 'Q': 2, 'U': 2, 'Z': 5},
    'X': {'K': 6, 'Q': 1, 'S': 5, 'U': 3},
    'Y': {'K': 5, 'R': 3, 'S': 6, 'V': 2},
    'Z': {'L': 1, 'R': 4, 'T': 3, 'W': 5}
}
#15.29411765
graph = {
"H211": {"H212": 4.25,"H213": 15.7},
"H212": {"H211":4.25, "H215":22.9},
"H213": {"H214":12, "H211": 15.7},
"H214": {"H213":12, "H215":11.4},
"H215": {"H212":22.9, "secondStairwellHS":15,"H214":11.4},
"secondStairwellHS": {"H215":15,"firstStairwellHS":11.7},
"firstStairwellHS": {"H115": 15, "secondStairwellHS":11.7, "groundStairwellHS": 11.7, "C101":21.6,"H121":17.7},
"groundStairwellHS": {"firstStairwellHS":11.7,},
"H111": {"H112": 4.25,"H113": 15.7},
"H112": {"H111":4.25, "H115":22.9},
"H113": {"H114":12, "H111": 15.7},
"H114": {"H113":12, "H115":11.4},
"H115": {"H112":22.9, "firstStairwellHS":15,"H114":11.4},
'C101': {"firstStairwellHS":21.6, "C102": 2.25},
'C102': {"C101":2.25, "C104": 11.1},
'C104': {"C102":11.1, "C105": 13},
'C105': {"C104":13, "C106": 13},
'C106': {"C105":13, "C107": 13},
'C107': {"C106":13, "H124": 40},
"H121": {"firstStairwellHS":17.7, "H122": 7.8,},
"H122": {"H121": 7.8,"H123": 8.5},
"H123": {"H122": 8.5,"H124": 8.5},
"H124": {"H123": 8.5,"C107": 40, "A114":46,"AA107":104.9,"E133":45},
"A114": {"H124":46, "A115": 29.4,"C162":29.4},
"A115": {"A114":29.4, },
"C162": {"A114":29.4, "C161": 2.25, "E113":39},
"C161": {"C162":2.25, "M101":29.4, "M011":32.6,"A015":38.6,},
"M101": {"C161":29.4, "M111": 5, "M011":32.6, "A015":38.6,},
"M111": {"M101":5, "M112": 5},
"M112": {"M111":5, "M113": 7, "M116": 14},
"M113": {"M112":7, "M115": 4},
"M115": {"M113":4},
"M116":{"M112":14, "M120":5},
"M120":{"M116":5, "M121":11.1, "M020": 21},
"M121":{"M120":11.1, "M123": 11.1},
"M123":{"M121":11.1},
"M020": {"M120":21, "M021": 11.1, "M014":7},
"M021": {"M020":11.1, "M022": 8},
"M022": {"M021":8, "M030": 3.5},
"M030": {"M022":3.5, },
"M014": {"M020":7, "M013": 9},
"M013": {"M014":9, "M012": 6},
"M012": {"M013": 6, "M011": 11.1},
"M011": {"M012":11.1, "M101":32.6, "C161": 32.6, "A015":27},
"A015": {"M011":27, "C161": 38.6, "M101":38.6, "A019": 13.7, "A016": 13, "A017": 12.4},
"A016": {"A015":13,"E010":28, "E013":28, "A018": 13.7},
"A017": {"A015":12.4, "A019": 12, "A018": 11.9},
"A019": {"A015":13.7, "A017": 12, },
"A018": {"A016":13.7, "A017":11.9,},
"E010": {"A016":28, "E013":7},
"E013": {"E010":7, "A016": 28, "E012":10.1},
"E012": {"E013":10.1, "E011": 10.1},
"E011": {"E012":10.1, "E021": 27,},
"E021": {"E022":12.4,"E011":27},
"E022": {"E021":12.4, "E023": 17, },
"E023": {"E022":17, "E031": 39, "E045":42.5},
"E045": {"E023":42.5, "E046": 10.2},
"E046": {"E045":10.2, "E047": 10.2},
"E047": {"E046":10.2, "E147": 39.2},

"AA107":{"AA106": 2.25, "AA105": 3,"H124":104.9, 'AA120':90},
"AA120": {"AA107":90, "AA119": 26, "AA022":36},
"AA119": {"AA120":26,},
"AA106": {"AA107": 2.25, "AA105": 1,},
"AA105": {"AA106": 1, "AA104": 16.3,"AA107": 3},
"AA104": {"AA105": 16.3, "AA001": 32.6, "AA003":32.6},
"AA001": {"AA003": 26, "AA104": 32.6 ,"AAGym":17, "AA022": 94.6, "AA020": 94.6},
"AA003": {"AA001": 26, "AA104":32.6, "AAGym":17},
"AAGym": {"AA001":17, "AA003":17,},
"AA022": {"AA020":26, "AA001": 94.6, "AA120": 36},
"AA020": {"AA022":26, "AA001": 94.6},


"E133":{"E132": 2.25, "H124":45},
"E132":{"E133":2.25, "E131": 11.1},
"E131":{"E132":11.1, "E145": 30, "E127": 29.4},
"E145":{"E131":30, "E146": 10, "E127": 29.4},
"E146":{"E145":10, "E147": 11},
"E147":{"E146":11,},
"E127":{"E131":29.4,"E145":29.4, "E100b": 22,"E126":16},
"E100b":{"E127":22, "E101":10.5},
"E126":{"E127":16, "E125": 10},
"E125":{"E123":4.5, "E126":10},
"E123":{"E125":4.5, "E122": 4},
"E122":{"E123":4, "E121": 3.5},
"E121":{"E122":3.5, "E101": 8},
"E101":{"E121":8, "E111": 14.5, "E100b":10.5},
"E111":{"E101":14.5, "E112": 13},
"E112":{"E111":13, "E113": 13},
"E113":{"E112":13, "C162":39},
}
#create a function that tests for internal consistency. You are going to get a much bigger graph, so this is important 
def consistency():

    for node in graph:
        for neighbor, weight in graph[node].items():
            if neighbor not in graph:
                print(f"Inconsistency @ {neighbor} ----- Not in graph but referenced by {node}")
            elif node not in graph[neighbor]:
                print(f"Inconsitency @ {node} ----- Links to neighbor but not the other way {neighbor}")
            elif graph[neighbor][node] != weight:
                print(f"Inconsistency: '{node}' to '{neighbor}' is {weight}, but '{neighbor}' to '{node}' is {graph[neighbor][node]}")
            else:
                pass

    


start = 'groundStairwellHS'
distances = {node: math.inf for node in graph}
consistency()
visited = []

distances[start] = 0


def dijikstra():
    unvisited = {node: distance for node, distance in distances.items() if node not in visited}
    currNode = min(unvisited, key=unvisited.get)
 
    for neighbor, edgeValue in graph[currNode].items():
        if neighbor not in visited:
            tempDistance = distances[currNode]+ edgeValue
            if tempDistance < distances[neighbor]:
                 distances[neighbor] = tempDistance
    visited.append(currNode)
    if(len(visited)<len(graph)):
        dijikstra()             
    else:
        print("Final distances", distances)

dijikstra()
elementaryFirst = ["E101","E111","E112","E113","E121","E122","E123","E124","E125","E126","E127","E131","E132","E133","E145","E146","E147"]
elementaryGround = ["E011","E012","E013","E021","E022","E023","E031","E032","E033","E045","E046","E047","E061","E066","E068","E069","E073","E074","E076"]
specialRooms = ["cafeteria","design","rynek", "annex gym", "main gym", "elementary gym","elementary garden"]
annexGround = ["AA001","AA003","AA020","AA022"]
annexFirst = ["AA103","AA104", "AA105", "AA106", "AA107","AA119","AA120"]
highschoolGround = ["H011","H012","H013","H014","H015","H021","H022","H023","H024"]
highschoolFirst = ["H111","H112","H113","H114","H115","H121","H122","H123","H124"]

middleschoolGround = ["M011","M012","M013","M014","M020","M021","M022","M030"]
middleschoolFirst = ["M101","M111","M112","M113","M115","M116","M120"]
adminGround = ["A015","A016","A017","A018","A019"]
adminFirst = ["A114","A115"]
highschoolSecond = ["H211", "H212", "H213", "H214","H215"]


