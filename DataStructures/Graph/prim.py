from DataStructures.Map import map_linear_probing as lp
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Graph import digraph as g
from DataStructures.Graph import prim_structure as ps

def prim(my_graph, source_key):

    g_order = g.order(my_graph)
    structure = ps.new_prim_structure(source_key, g_order)

    keys = g.vertices(my_graph)
    for key in keys:
        lp.put(structure["dist_to"], key, float("inf"))
        lp.put(structure["marked"], key, False)

    lp.put(structure["dist_to"], source_key, 0.0)
    pq.insert(structure["pq"], source_key, 0.0)

    while not pq.is_empty(structure["pq"]):
        current = pq.del_min(structure["pq"])
        current_vertex = current["key"]
        lp.put(structure["marked"], current_vertex, True)

        neighbors = g.adjacents(my_graph, current_vertex)
        neighbor_keys = lp.key_set(neighbors)

        for neighbor_key in neighbor_keys:
            is_marked = lp.get(structure["marked"], neighbor_key)
            edge = g.get_edge(my_graph, current_vertex, neighbor_key)
            weight = edge["weight"]
            current_dist = lp.get(structure["dist_to"], neighbor_key)

            if not is_marked and weight < current_dist:
                lp.put(structure["dist_to"], neighbor_key, weight)
                lp.put(structure["edge_from"], neighbor_key, edge)
                pq.insert(structure["pq"], neighbor_key, weight)

    return structure