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
            self.weights[(node1, node2)] = weight 
            self.adj[node2].append(node1)  
            self.weights[(node2, node1)] = weight 

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)

def distance(station_list, station1, station2):
    #the station_list isn't perfectly sorted and i'm not sure how to sort since it has a bunch of attributes attached
    #todo: fix it to make this more efficient? but it does the job for now
    target1 = 0
    target2 = 0
    for station in station_list: #searching for stations in the station list, just linear search bc not sorted
        if int(station1) == int(station[0]):
            target1 = station
        elif int(station2) == int(station[0]):
            target2 = station
        if target1 != 0 and target2 != 0:
            break
    
    lat1 = float(target1[1])
    long1 = float(target1[2])
    lat2 = float(target2[1])
    long2 = float(target2[2])
    distance = math.sqrt((lat2-lat1)**2 + (long2-long1)**2)
    return distance

def main():
    filepath1 = Path(__file__).parent / "london_connections.csv"
    filepath2 = Path(__file__).parent / "london_stations.csv"

    file1 = open(filepath1, 'r')
    file2 = open(filepath2, 'r')

    connections = csv.reader(file1)
    num_connections = 0
    connection_list = []
    for row in connections:
        num_connections += 1
        connection_list.append(row)
    num_stations = 0
    station_list = []
    stations = csv.reader(file2)
    for row in stations:
        num_stations += 1
        station_list.append(row)
    del connection_list[0]
    del station_list[0]
    #these two lines just delete the "header" lines in the csv files

    subway = UndirectedWeightedGraph()
    num_nodes = len(station_list)

    for i in range(1, num_nodes + 2):
        subway.add_node(i)
    
    for connect in connection_list:
        station1 = int(connect[0])
        station2 = int(connect[1])
        weight = distance(station_list, station1, station2)
        subway.add_edge(station1, station2, weight)
        print([station1, station2, weight])

    print("Subway map initialized")

    
main()