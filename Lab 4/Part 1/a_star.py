from final_project_part1 import *

def total_cost(h, dist, node_cost):
    cost = {}

    # add the distance and heuristic function
    for i in node_cost:
        cost[node_cost[i]] = dist[node_cost[i]] + h[node_cost[i]]

    # sort nodes by dictionary value which contains the total cost 
    sorted_dict = sorted(cost.items(), key=lambda cost: cost[1])

    # loop through the sorted dictionary and only extract the node number
    for node in sorted_dict:
        return node[0]

# using Dijkstra's with an addition of the heuristic 
def a_star(G, s, d, h):
    pred = {}
    dist = {}
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(s, 0)

    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key

        # case where node being searched is starting node
        if current_node == d:
            break

        node_path = total_cost(h, dist, G.adj[current_node])
        for neighbour in node_path:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return pred, dist