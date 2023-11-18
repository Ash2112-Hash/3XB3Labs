
from final_project_part1 import *


def dijkstra_approx(G, source, k):
    dist = {}
    Q = min_heap.MinHeap([])
    G_nodes = list(G.adj.keys())
    relaxedCount = k

    for node in G_nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    while not Q.is_empty() and relaxedCount != 0:
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key

        for neighbour in G.adj[current_node]:
            if (dist[current_node] + G.w(current_node, neighbour)) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)

        relaxedCount -= 1

    return dist






for _ in range(100):
    G = create_random_complete_graph(10, 200)
    print(G.adj)
    print(G.weights)
    print(dijkstra(G, 0))
    print(dijkstra_approx(G, 0, 1))
    assert dijkstra(G, 0) != dijkstra_approx(G, 0, 1)