from DataStructures.Graph import digraph as g
from DataStructures.Stack import stack
from DataStructures.Map import map_linear_probing as lp

def dfs(my_graph, source):
    visited_map = lp.new_map(num_elements=g.order(my_graph), load_factor=0.5)
    
    lp.put(visited_map, source, {"marked": True, "edge_from": None})
    
    dfs_vertex(my_graph, source, visited_map)
    
    return visited_map

def dfs_vertex(my_graph, vertex, visited_map):

    neighbors = g.adjacents(my_graph, vertex)
    
    if neighbors is not None:
    
        for neighbor in neighbors:
            if not lp.contains(visited_map, neighbor):
                lp.put(visited_map, neighbor, {"marked": True, "edge_from": vertex})
                dfs_vertex(my_graph, neighbor, visited_map)


def has_path_to(key_v, visited_map):
    return lp.contains(visited_map, key_v)

def path_to(key_v, visited_map):
    if not has_path_to(key_v, visited_map):
        return None
    
    path = stack.new_stack()
    current = key_v
    while current is not None:
        stack.push(path, key_v)
        current = lp.get(visited_map, current)["edge_from"]
        
    return path
