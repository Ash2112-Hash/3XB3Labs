from subway_map import *
from final_project_part1 import *
from algorithms import *
import matplotlib.pyplot as plot
import random
import timeit

def main():
    subway_graph = create()
    graph = subway_graph[0]
    station_list = subway_graph[1]
    lines = subway_graph[2]
    heuristics = heuristic(station_list)
    all_pairs_test(graph, station_list, heuristics)
    same_line_test(graph, heuristics, lines, 9) # 9 is arbitrarily chosen
    adj_line(2, 3, lines) # test case, evaluates to True
    adj_line_test(graph, heuristics, lines, 3) # since it is adjacent to line 2
    num_transfer(lines, 193) # test case, evaluates to 4
    transfer_lines_test(graph, heuristics, lines, 5, 193) # line 5 is one of the lines station 193 is on

# all pairs of A*
def all_pairs_a_star(graph, station, heuristic_dict): # use an index of the heuristic
    all_pairs = {}
    for node in station.keys():
        path = {}
        for connected_node in station.keys():
            pairs = a_star(graph, int(station[node][0]), int(station[connected_node][0]), heuristic_dict[connected_node])
            path[connected_node] = pairs
        all_pairs[node] = path
    return all_pairs

# all pairs of dijkstra
def all_pairs_dijkstra(graph, station):
    all_pairs = {}

    for node in station:
        pairs = dijkstra(graph, node)
        all_pairs[node] = pairs
    return all_pairs

# on adjacent lines
def adj_line(lineOne, lineTwo, lines):
    if lines[lineOne].intersection(lines[lineTwo]) != set():
        return True
    return False

# on transfer lines, counting number of transfers
def num_transfer(lines, station_num):
    j = station_num
    counter = 0
    for i in lines.keys():
        if j in lines.get(i):
            counter += 1
    return counter

# tests
def all_pairs_test(graph, station, heuristic_dict):
    start_time = timeit.default_timer()
    all_pairs_a_star(graph, station, heuristic_dict)
    end_time = timeit.default_timer()
    a_star_time = end_time - start_time

    start_time = timeit.default_timer()
    all_pairs_dijkstra(graph, station)
    end_time = timeit.default_timer()
    dijkstra_time = end_time - start_time

    print("a star all pairs shortest path time:", a_star_time, "seconds")
    print("dijkstra all pairs shortest path time:", dijkstra_time, "seconds")

def same_line_test(graph, heuristic_dict, lines, line_num):
    random_station = 277 # station on line 9, start station
    stations_visited = random.sample(list(lines[line_num]), 10)

    a_star_time = []
    dijkstra_time = []
    a_star_sum = 0
    dijkstra_sum = 0

    for n in stations_visited:
        a_star_sum, dijkstra_sum = 0, 0

        start_time = timeit.default_timer()
        a_star(graph, random_station, n, heuristic_dict[n])
        end_time = timeit.default_timer()
        a_star_sum += (end_time - start_time)

        start_time = timeit.default_timer()
        new_dijkstra(graph, random_station, n)
        end_time = timeit.default_timer()
        dijkstra_sum += (end_time - start_time)

        a_star_time.append(a_star_sum)
        dijkstra_time.append(dijkstra_sum)

    plot.plot([str(i) for i in stations_visited], a_star_time, label = 'A*')
    plot.plot([str(i) for i in stations_visited], dijkstra_time, label = 'Dijkstra')
    plot.legend(loc = 'upper left', title = 'Algorithms', fontsize = 10)
    plot.xlabel('Station Number')
    plot.ylabel('Runtime (seconds)')
    plot.title("Runtime vs Station on Same Line")
    plot.show()

def adj_line_test(graph, heuristic_dict, lines, line_num):
    random_station = 76 # station on line 2, start station
    stations_visited = random.sample(list(lines[line_num]), 10)

    a_star_time = []
    dijkstra_time = []
    a_star_sum = 0
    dijkstra_sum = 0

    for n in stations_visited:
        a_star_sum, dijkstra_sum = 0, 0

        start_time = timeit.default_timer()
        a_star(graph, random_station, n, heuristic_dict[n])
        end_time = timeit.default_timer()
        a_star_sum += (end_time - start_time)

        start_time = timeit.default_timer()
        dijkstra(graph, random_station)
        end_time = timeit.default_timer()
        dijkstra_sum += (end_time - start_time)

        a_star_time.append(a_star_sum)
        dijkstra_time.append(dijkstra_sum)

    plot.plot([str(i) for i in stations_visited], a_star_time, label = 'A*')
    plot.plot([str(i) for i in stations_visited], dijkstra_time, label = 'Dijkstra')
    plot.legend(loc = 'upper left', title = 'Algorithms', fontsize = 10)
    plot.xlabel('Station Number')
    plot.ylabel('Runtime (seconds)')
    plot.title("Runtime vs Station on Adjacent Lines")
    plot.show()

def transfer_lines_test(graph, heuristic_dict, lines, line_num, station_num):
    start_station = station_num
    transfers = 5
    stations_visited = random.sample(list(lines[line_num]), transfers)

    a_star_time = []
    dijkstra_time = []
    a_star_sum = 0
    dijkstra_sum = 0

    for n in stations_visited:
        a_star_sum, dijkstra_sum = 0, 0

        start_time = timeit.default_timer()
        a_star(graph, start_station, n, heuristic_dict[n])
        end_time = timeit.default_timer()
        a_star_sum += (end_time - start_time)

        start_time = timeit.default_timer()
        dijkstra(graph, start_station)
        end_time = timeit.default_timer()
        dijkstra_sum += (end_time - start_time)

        a_star_time.append(a_star_sum)
        dijkstra_time.append(dijkstra_sum)

    plot.plot([str(i) for i in range(transfers)], a_star_time, label = 'A*')
    plot.plot([str(i) for i in range(transfers)], dijkstra_time, label = 'Dijkstra')
    plot.legend(loc = 'upper left', title = 'Algorithms', fontsize = 10)
    plot.xlabel('Number of Transfers')
    plot.ylabel('Runtime (seconds)')
    plot.title("Runtime vs Station on Transfer Lines")
    plot.show()

if __name__ == "__main__":
    main()