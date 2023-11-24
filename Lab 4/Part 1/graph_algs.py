
from final_project_part1 import *


def dijkstra_approx(G, source, k):
    dist = {}
    Q = min_heap.MinHeap([])
    G_nodes = list(G.adj.keys())
    relaxedCount = {}

    for node in G_nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
        relaxedCount[node] = 0
    Q.decrease_key(source, 0)

    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key

        if relaxedCount[current_node] < k:
            for neighbour in G.adj[current_node]:
                if (dist[current_node] + G.w(current_node, neighbour)) < dist[neighbour] and relaxedCount[neighbour] < k:
                    Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                    relaxedCount[neighbour] += 1
        else:
            continue

    #print("track relax node count:", relaxedCount)
    #print("node distances: ", dist)
    return dist


def bellman_ford_approx(G, source, k):
    dist = {}
    G_nodes = list(G.adj.keys())
    relaxedCount = {}

    for node in G_nodes:
        dist[node] = float("inf")
        relaxedCount[node] = 0
    dist[source] = 0

    for _ in range(G.number_of_nodes()):   #TODO confirm if this needs to be replaced by k
        for node in G_nodes:
            if relaxedCount[node] < k:
                for neighbour in G.adj[node]:
                    if dist[neighbour] > dist[node] + G.w(node, neighbour) and relaxedCount[neighbour] < k:
                        dist[neighbour] = dist[node] + G.w(node, neighbour)
                        relaxedCount[neighbour] += 1
            else:
                continue

    #print("track relax node count:", relaxedCount)
    #print("node distances: ", dist)
    return dist


"""
#TESTING
for _ in range(1):
    G = create_random_complete_graph(20, 200)
    print(dijkstra(G, 0))

    print(total_dist(dijkstra(G, 0)))
    print(total_dist(dijkstra_approx(G, 0, 2)))
    #r = dijkstra_approx(G, 0, 1)

    #print(dijkstra(G, 0))
    #print(r[0])
    #print(bellman_ford_approx(G, 0, 3))
    #print(G.adj)
    #print(G.weights)
    #print(dijkstra(G, 0))
    #print(dijkstra_approx(G, 0, 1))
    #print(bellman_ford_approx(G, 0, 1))
    #assert dijkstra(G, 0) != dijkstra_approx(G, 0, 1)
"""