from DataStructures.Map import map_linear_probing as lp
from DataStructures.List import array_list as al
from DataStructures.Graph import digraph as g
from DataStructures.Graph import dfo_structure as structure
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as s

def dfo(my_graph):
    aux_structure = structure.new_dfo_structure(g.order(my_graph))
    lista_vert = g.vertices(my_graph)
    
    for i in range(al.size(lista_vert)):
        vertex = al.get_element(lista_vert, i)
        if not lp.contains(aux_structure["marked"], vertex):
            dfs_vertex(my_graph, vertex, aux_structure)
        
    return aux_structure
    
    
def dfs_vertex(my_graph, key_v, aux_structure):
    q.enqueue(aux_structure["pre"], key_v)

    lp.put(aux_structure["marked"], key_v, True)

    neighbors = g.adjacents(my_graph, key_v)
    for i in range(al.size(neighbors)):
        neighbor = al.get_element(neighbors, i)
        if not lp.contains(aux_structure["marked"], neighbor):
            dfs_vertex(my_graph, neighbor, aux_structure)
            
    q.enqueue(aux_structure["post"], key_v)
    s.push(aux_structure["reversepost"], key_v)