import csv
from pathlib import Path
import math

class UndirectedWeightedGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)
        self.weights[(node1, node2)] = weight   
        self.weights[(node2, node1)] = weight 

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)

def distance(station1, station2):
    distance = math.sqrt((float(station2[1])-float(station1[1]))**2 + (float(station2[2])-float(station1[2]))**2)
    return distance

def heuristic(station_list):
    heuristics = {}

    for i in station_list.keys():
        distance_list = {}
        for j in station_list.keys():
            cost = distance(station_list[i], station_list[j])
            distance_list[j] = cost
        heuristics[i] = distance_list
    return heuristics

def create():
    filepath1 = Path(__file__).parent / "london_connections.csv"
    filepath2 = Path(__file__).parent / "london_stations.csv"

    file1 = open(filepath1, 'r')
    file2 = open(filepath2, 'r')

    station_list = {}
    lines = {}
    stations = csv.reader(file2)
    next(stations, None) #skips header
    for row in stations:
        station_id = int(row[0])
        station_list[station_id] = row
    file2.close()

    connections = csv.reader(file1)
    next(connections, None)

    subway = UndirectedWeightedGraph()
    num_nodes = len(station_list)

    for i in range(1, num_nodes + 2):
        subway.add_node(i)
    
    for connect in connections:
        station1 = station_list[int(connect[0])]
        station2 = station_list[int(connect[1])]
        line = int(connect[2])
        if line not in lines:
            lines[line] = set()
        lines[line].add(int(connect[0]))
        lines[line].add(int(connect[1]))
        weight = distance(station1, station2)
        subway.add_edge(int(station1[0]), int(station2[0]), weight)
    
    return (subway, station_list, lines)