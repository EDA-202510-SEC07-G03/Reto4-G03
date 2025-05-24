from DataStructures.Graph import digraph as g
from DataStructures.Stack import stack
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Queue import queue

def bfs(my_graph, source):
    visited_map = lp.new_map(num_elements=g.order(my_graph), load_factor=0.5)
    
    lp.put(visited_map, source, {"edge_from": None, "dist_to": 0})
    
    visited_map = bfs_vertex(my_graph, source, visited_map)
    
    return visited_map

def bfs_vertex(my_graph, source, visited_map):
    q = queue.new_queue()
    queue.enqueue(q, source)

    while not queue.is_empty(q):
        vertex = queue.dequeue(q)
        neighbors = g.adjacents(my_graph, vertex)

        for neighbor in neighbors:
            if not lp.contains(visited_map, neighbor):
                prev = lp.get(visited_map, vertex)
                lp.put(visited_map, neighbor, {
                    "edge_from": vertex,
                    "dist_to": prev["dist_to"] + 1
                })
                queue.enqueue(q, neighbor)
    
    return visited_map

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
