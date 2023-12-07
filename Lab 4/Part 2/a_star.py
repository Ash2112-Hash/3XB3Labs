from final_project_part1 import *

def total_cost(h, dist, node_cost):
    cost = {}
    cost_order = []

    # add the distance and heuristic function
    for i in node_cost:
        cost[i] = dist[i] + h[i]

    # sort nodes by dictionary value which contains the total cost 
    sorted_dict = sorted(cost.items(), key=lambda cost: cost[1])

    # loop through the sorted dictionary and only extract the node number
    for node in sorted_dict:
        cost_order.append(node[0])

    return cost_order

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

    path, current_node = [], d
    while current_node and current_node != s:
        path.append(current_node)
        current_node = pred.get(current_node, None)
    path = path[::-1]

    return (pred, path)