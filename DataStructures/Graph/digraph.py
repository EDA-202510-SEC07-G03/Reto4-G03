from DataStructures.Map import map_linear_probing as lp
from DataStructures.Map import map_functions as map
from DataStructures.Graph import edge as ed
from DataStructures.Graph import vertex as vt

def new_graph(order):
    graph = {
        "vertices": lp.new_map(order, 0.5),
        "num_edges": 0,
    }
    return graph

def insert_vertex(my_graph, key_u, info_u):
    vertex = vt.new_vertex(key_u, info_u)
    lp.put(my_graph["vertices"], key_u, vertex)
    print("Vertice insertado")
    print(lp.get(my_graph["vertices"], key_u))
    return my_graph

def update_vertex_info(my_graph, key_u, new_info_u):
    if lp.contains(my_graph["vertices"], key_u):
        vertex = lp.get(my_graph["vertices"], key_u)
        vt.set_value(vertex, new_info_u)
        retorno = my_graph
    else:
        retorno = None
    return retorno

def remove_vertex(my_graph, key_u):
    if lp.contains(my_graph["vertices"], key_u):
        lp.remove(my_graph["vertices"], key_u)
        for key in lp.key_set(my_graph["vertices"]):
            hash = map.hash_value(my_graph["vertices"], key)
            vertex = my_graph["vertices"]["table"]["elements"][hash]
            edges = vt.get_adjacents(vertex)
            if lp.contains(edges, key_u):
                lp.remove(edges, key_u)
                my_graph["num_edges"] -= 1
    return my_graph

def add_edge(my_graph, key_u, key_v, weight=1.0):
    if not lp.contains(my_graph["vertices"], key_u):
        raise Exception("El vertice u no existe")
    if not lp.contains(my_graph["vertices"], key_v):
        raise Exception("El vertice v no existe")
    nodo = lp.get(my_graph["vertices"], key_u)
    edges = vt.get_adjacents(nodo)
    if lp.contains(edges, key_v):
        arco = vt.get_edge(nodo, key_v)
        arco["weight"] = weight
    else:
        vt.add_adjacent(nodo, key_v, weight)
        my_graph["num_edges"] += 1
    return my_graph

def order(my_graph):
    return lp.size(my_graph["vertices"])

def size(my_graph):
    return my_graph["num_edges"]

def vertices(my_graph):
    return lp.key_set(my_graph["vertices"])

def degree(my_graph, key_u):
    if lp.contains(my_graph["vertices"], key_u):
        nodo = lp.get(my_graph["vertices"], key_u)
        return vt.degree(nodo)
    else:
        raise Exception("El vertice no existe")
    
def get_edge(my_graph, key_u, key_v):
    if not lp.contains(my_graph["vertices"], key_u):
        raise Exception("El vertice u no existe")
    hash = map.hash_value(my_graph["vertices"], key_u)
    vertice = my_graph["vertices"]["table"]["elements"][hash]
    return vt.get_edge(vertice, key_v)

def get_vertex_information(my_graph, key_u):
    if not lp.contains(my_graph["vertices"], key_u):
        raise Exception("El vertice no existe")
    vertice = lp.get(my_graph["vertices"], key_u)
    return vertice

def contains_vertex(my_graph, key_u):
    return lp.contains(my_graph["vertices"], key_u) 

def adjacents(my_graph, key_u):
    if not lp.contains(my_graph["vertices"], key_u):
        raise Exception("El vertice no existe")
    print("Adjacentes ante")
    print(str(lp.get(my_graph["vertices"], key_u)))
    nodo = lp.get(my_graph["vertices"], key_u)['value']['adjacents']
    return nodo

def edges_vertex(my_graph, key_u):
    if not lp.contains(my_graph["vertices"], key_u):
        raise Exception("El vertice no existe")
    hash = map.hash_value(my_graph["vertices"], key_u)
    vertex = my_graph["vertices"]["table"]["elements"][hash]
    map = vt.get_adjacents(vertex)
    return lp.value_set(map) 

def get_vertex(my_graph, key_u):
    if not lp.contains(my_graph["vertices"], key_u):
        raise Exception("El vertice no existe")
    return lp.get(my_graph["vertices"], key_u)



    
    
