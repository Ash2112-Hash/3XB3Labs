
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
                if (dist[current_node] + G.w(current_node, neighbour)) < dist[neighbour]:
                    Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                    relaxedCount[neighbour] += 1
        else:
            continue

    return dist


def bellman_ford_approx(G, source, k):
    dist = {}
    G_nodes = list(G.adj.keys())
    relaxedCount = {}

    for node in G_nodes:
        dist[node] = float("inf")
        relaxedCount[node] = 0
    dist[source] = 0

    for _ in range(G.number_of_nodes()):
        for node in G_nodes:
            if relaxedCount[node] < k:
                for neighbour in G.adj[node]:
                    if dist[neighbour] > dist[node] + G.w(node, neighbour):
                        dist[neighbour] = dist[node] + G.w(node, neighbour)
                        relaxedCount[neighbour] += 1
            else:
                continue

    return dist



"""TESTING"""
for _ in range(100):
    G = create_random_complete_graph(10, 200)
    print(G.adj)
    print(G.weights)
    print(dijkstra(G, 0))
    print(dijkstra_approx(G, 0, 1))
    print(bellman_ford_approx(G, 0, 1))
    assert dijkstra(G, 0) != dijkstra_approx(G, 0, 1)
