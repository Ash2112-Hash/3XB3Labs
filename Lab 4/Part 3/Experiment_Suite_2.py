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
    transfer = subway_graph[3]
    heuristics = heuristic(station_list)

    # test 1: all-pairs
    all_pairs_test(graph, station_list, heuristics)

    # test 2: same line
    same_line_test(graph, heuristics, lines, 9) # 9 is arbitrarily chosen

    # test 3: adjacent lines
    adj_line(2, 3, lines) # test case, evaluates to True
    adj_line_test(graph, heuristics, lines, 3) # since it is adjacent to line 2

    # test 4: multiple transfers
    zero_transfer = a_star_new(subway_graph[0], 294, 138, heuristics[138]) # test case, returns 0
    num_of_transfers(zero_transfer[1], transfer)
    one_transfer = a_star_new(subway_graph[0], 1, 176, heuristics[176]) # test case, returns 1
    num_of_transfers(one_transfer[1], transfer)
    two_transfer = a_star_new(subway_graph[0], 36, 120, heuristics[120]) # test case, returns 2
    num_of_transfers(two_transfer[1], transfer)
    three_transfer = a_star_new(subway_graph[0], 181, 2, heuristics[2]) # test case, returns 3
    num_of_transfers(three_transfer[1], transfer)
    four_transfer = a_star_new(subway_graph[0], 137, 148, heuristics[148]) # test case, returns 4
    num_of_transfers(four_transfer[1], transfer)
    five_transfer = a_star_new(subway_graph[0], 19, 2, heuristics[2]) # test case, returns 5
    num_of_transfers(five_transfer[1], transfer)
    transfer_lines_test(subway_graph[0], heuristics)

# all pairs of A*
def all_pairs_a_star(graph, station, heuristic_dict):
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
def num_of_transfers(path, transfer):
    line_num = set()
    for i in range(len(path) - 1):
        station1 = path[i]
        station2 = path[i + 1]
        for j in range(len(transfer)):
            if ((station1 == transfer[j][0]) and (station2 == transfer[j][1])) or ((station1 == transfer[j][1]) and (station2 == transfer[j][0])):
                line_num.add(transfer[j][2])
    return len(line_num)

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

def transfer_lines_test(graph, heuristic_dict):
    start_node = [294, 1, 36, 181, 137, 19] # from test cases
    end_node = [138, 176, 120, 2, 148, 2] # from test cases

    a_star_time = []
    dijkstra_time = []
    a_star_sum = 0
    dijkstra_sum = 0

    for i in range(len(start_node)):
        a_star_sum, dijkstra_sum = 0, 0

        start_time = timeit.default_timer()
        a_star(graph, start_node[i], end_node[i], heuristic_dict[end_node[i]])
        end_time = timeit.default_timer()
        a_star_sum += (end_time - start_time)

        start_time = timeit.default_timer()
        dijkstra(graph, start_node[i])
        end_time = timeit.default_timer()
        dijkstra_sum += (end_time - start_time)

        a_star_time.append(a_star_sum)
        dijkstra_time.append(dijkstra_sum)

    plot.plot([str(i) for i in range(len(start_node))], a_star_time, label = 'A*')
    plot.plot([str(i) for i in range(len(start_node))], dijkstra_time, label = 'Dijkstra')
    plot.legend(loc = 'upper left', title = 'Algorithms', fontsize = 10)
    plot.xlabel('Number of Transfers')
    plot.ylabel('Runtime (seconds)')
    plot.title("Runtime vs Station on Transfer Lines")
    plot.show()

if __name__ == "__main__":
    main()