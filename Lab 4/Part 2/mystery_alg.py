import final_project_part1
import graph
import matplotlib.pyplot as plt
import timeit


# ******Graphing*******

def test_mystery(graph_size, average_runs):
    graph_sizes = []
    search_times = []

    for i in range(graph_size):
        graph_edges = i * 2 # always twice as many edges as nodes
        G = final_project_part1.create_random_complete_graph(i, graph_edges)
        graph_sizes.append(i)
        search_time_sum = 0

        for i in range(average_runs): #running the experiment multiple times for more accuracy
            H = G
            start = timeit.default_timer()
            d = final_project_part1.mystery(H)
            end = timeit.default_timer()
            search_time_sum += (end-start)

        search_times.append(search_time_sum/average_runs)

    #plotting the graph
    plt.plot(graph_sizes, search_times)
    plt.xlabel('Number of Vertices')
    plt.ylabel('Average Runtime (seconds)')
    plt.title('Runtime of Mystery Algorithm')
    plt.show()
    return None

def main():
    test_mystery(60, 200)

main()