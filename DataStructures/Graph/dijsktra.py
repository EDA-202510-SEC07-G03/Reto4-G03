from DataStructures.Map import map_linear_probing as lp
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Graph import digraph as g
from DataStructures.Graph import dijsktra_structure as ds

def dijkstra(my_graph, source_key):
    g_order = g.order(my_graph)
    structure = ds.new_dijsktra_structure(source_key, g_order)

    lp.put(structure["visited"], source_key, 0)
    pq.insert(structure["pq"], source_key, 0)

    while not pq.is_empty(structure["pq"]):
        current = pq.del_min(structure["pq"])
        current_vertex = current["key"]
        current_distance = current["priority"]

        neighbors_map = g.adjacents(my_graph, current_vertex)
        neighbors_keys = lp.key_set(neighbors_map)

        for neighbor in neighbors_keys:
            edge = g.get_edge(my_graph, current_vertex, neighbor)
            weight = edge["weight"]
            distance = current_distance + weight

            if not lp.contains(structure["visited"], neighbor):
                lp.put(structure["visited"], neighbor, distance)
                pq.insert(structure["pq"], neighbor, distance)
            else:
                existing_distance = lp.get(structure["visited"], neighbor)
                if distance < existing_distance:
                    lp.put(structure["visited"], neighbor, distance)
                    pq.insert(structure["pq"], neighbor, distance)

    return structure