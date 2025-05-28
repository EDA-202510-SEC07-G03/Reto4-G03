import time
import csv
import os
from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as al
from DataStructures.Graph import digraph as dg
from DataStructures.Graph import dfo as dfo
from DataStructures.Graph import dfs as dfs
from DataStructures.Graph import bfs as bfs
from DataStructures.Graph import dijsktra as dij
from DataStructures.Graph import prim as prim
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog ={"registros": al.new_list(),
              "grafo": dg.new_graph(1000)}
    return catalog

# Funciones para la carga de datos

def load_data(catalog, filename=(data_dir + "deliverytime_min.csv")):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    file = open(filename, encoding="utf-8")
    restaurants = al.new_list()
    domicilios = al.new_list()
    rappis = al.new_list()
    reader = csv.DictReader(file)
    t_total = 0
    t_counter = 0
    for row in reader:
        delivery ={
            "ID": row["ID"],
            "Delivery_person_ID": row["Delivery_person_ID"],
            "Delivery_person_Age": row["Delivery_person_Age"],
            "Delivery_person_Ratings": row["Delivery_person_Ratings"],
            "Restaurant_latitude": row["Restaurant_latitude"],
            "Restaurant_longitude": row["Restaurant_longitude"],
            "Delivery_location_latitude": row["Delivery_location_latitude"],
            "Delivery_location_longitude": row["Delivery_location_longitude"],
            "Type_of_order": row["Type_of_order"],
            "Type_of_vehicle": row["Type_of_vehicle"],
            "Time_taken": int(row["Time_taken(min)"]),
        }
        al.add_last(catalog["registros"], delivery)
        if row["Delivery_person_ID"] not in rappis:
            al.add_last(rappis, row["Delivery_person_ID"])
        r_loctation = (row["Restaurant_latitude"]+"_"+row["Restaurant_longitude"])
        d_location = (row["Delivery_location_latitude"]+"_"+row["Delivery_location_longitude"])
        if r_loctation not in restaurants:
            al.add_last(restaurants, row["Restaurant_latitude"])
        if d_location not in domicilios:
            al.add_last(domicilios, row["Delivery_location_latitude"])
        t_total += int(row["Time_taken(min)"])
        t_counter += 1
    t_avg = t_total / t_counter
    file.close()
    return al.size(catalog["registros"]), al.size(rappis), al.size(restaurants), al.size(domicilios),  t_avg

# Funciones de consulta sobre el catálogo

def decimales(numero):
    num = float(numero)
    return f"{num:.4f}"

def diagraph(catalog):
    """
    crea el digrafo de los domicilios y restaurantes
    """
    graph = catalog["grafo"]
    registros = catalog["registros"]
    for i in range(al.size(registros)):
        r_latt = decimales(registros["elements"][i]["Restaurant_latitude"])
        r_long = decimales(registros["elements"][i]["Restaurant_longitude"])
        d_latt = decimales(registros["elements"][i]["Delivery_location_latitude"])
        d_long = decimales(registros["elements"][i]["Delivery_location_longitude"])
        r_location = (r_latt+"_"+r_long)
        d_location = (d_latt+"_"+d_long)
        if not dg.contains_vertex(graph, r_location):
            value = al.new_list()
            al.add_last(value, registros["elements"][i]["ID"])
            dg.insert_vertex(graph, r_location, value)
        else:
            valor = dg.get_vertex_information(graph, r_location)
            al.add_last(valor["value"], registros["elements"][i]["ID"])
        adj_r = dg.adjacents(graph, r_location)
        if not dg.contains_vertex(graph, d_location):
            value = al.new_list()
            al.add_last(value, registros["elements"][i]["ID"])
            dg.insert_vertex(graph, d_location, value)
        else:
            valor = dg.get_vertex_information(graph, d_location)
            al.add_last(valor["value"], registros["elements"][i]["ID"])
        adj_d = dg.adjacents(graph, d_location)
        if not mp.contains(adj_r, d_location) and not mp.contains(adj_d, r_location):
            dg.add_edge(graph, r_location, d_location, registros["elements"][i]["Time_taken"])
            dg.add_edge(graph, d_location, r_location, registros["elements"][i]["Time_taken"])
        else:
            arco = dg.get_edge(graph, r_location, d_location)
            peso_1 = arco["weight"]
            nuevo_peso = (peso_1 + registros["elements"][i]["Time_taken"]) / 2
            arco["weight"] = nuevo_peso
            arco_2 = dg.get_edge(graph, d_location, r_location)
            peso_2 = arco_2["weight"]
            nuevo_peso_2 = (peso_2 + registros["elements"][i]["Time_taken"]) / 2
            arco_2["weight"] = nuevo_peso_2
    return mp.size(graph["vertices"])
 
def conexion_domicilios(catalog, graph):
    graph = catalog["grafo"]
    registros = catalog["registros"]
    i = 0
    while i < al.size(catalog):
        centinela = False
        j = i + 1
        while not centinela and j <= al.size(catalog):
            if registros["elements"][i]["Delivery_location_latitude"] == registros["elements"][j]["Delivery_location_latitude"] and registros[i]["Delivery_location_longitude"] == registros[j]["Delivery_location_longitude"]:    
                d1_lat = decimales(registros["elements"][i]["Delivery_location_latitude"])
                d1_long = decimales(registros["elements"][i]["Delivery_location_longitude"])
                r1_lat = decimales(registros["elements"][i]["Restaurant_latitude"])
                r1_long = decimales(registros["elements"][i]["Restaurant_longitude"])
                d2_lat = decimales(registros["elements"][j]["Delivery_location_latitude"])
                d2_long = decimales(registros["elements"][j]["Delivery_location_longitude"])
                r2_lat = decimales(registros["elements"][j]["Restaurant_latitude"])
                r2_long = decimales(registros["elements"][j]["Restaurant_longitude"])
                d1_location = (d1_lat + "_" + d1_long)
                r1_location = (r1_lat + "_" + r1_long)
                d2_location = (d2_lat + "_" + d2_long)
                r2_location = (r2_lat + "_" + r2_long)
                arco_d1 = dg.get_edge(graph, d1_location, r1_location)
                peso_1 = arco_d1["weight"]
                arco_d2 = dg.get_edge(graph, d2_location, r2_location)
                peso_2 = arco_d2["weight"]
                nuevo_peso = (peso_1 + peso_2) / 2
                dg.add_edge(graph, d1_location, d2_location, nuevo_peso)
                dg.add_edge(graph, d2_location, d1_location, nuevo_peso)
                centinela = True
            else:
                j += 1
        i+= 1
    return graph["num_edges"]
                

def req_1(catalog, id_a, id_b):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time = get_time()
    conections = dfs.dfs(catalog["grafo"], id_a)
    path = dfs.path_to(id_b, conections)
    if path is None:
        end_time = get_time()
        time = delta_time(start_time, end_time)
        return None, time
    else:
        restaurants = al.new_list()
        node = path["first"]
        ids = al.new_list()
        while node is not None:
            i = 0
            centinela = False
            while not centinela:
                if catalog["registros"]["elements"][i]["ID"] == node["info"]:
                    lat_1 = decimales(catalog["registros"]["elements"][i]["Restaurant_location_latitude"])
                    long_1 = decimales(catalog["registros"]["elements"][i]["Restaurant_location_longitude"])
                    key = (lat_1 + "_" + long_1)
                    if mp.contains(conections["marked"], key):
                        al.add_last(restaurants, key)
                    if catalog["registros"]["elements"][i]["Delivery_person_ID"] not in ids:
                        al.add_last(ids, catalog["registros"]["elements"][i]["Delivery_person_ID"])
                        centinela = True    
                i += 1
            node = node["next"]
        end_time = get_time()
        time = delta_time(start_time, end_time)
        return ids, path["size"], path["elements"], restaurants, time
        
    


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog, id):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = get_time()
    centinela = False
    j = 0
    while not centinela and j < al.size(catalog["registros"]):
        if catalog["registros"]["elements"][j]["ID"] == id:
            lat = catalog["registros"]["elements"][j]["Restaurant_latitude"]
            long = catalog["registros"]["elements"][j]["Restaurant_longitude"]
            centinela = True
        else:
            j += 1
    if not centinela:
        end_time = get_time()
        time = delta_time(start_time, end_time)
        return None, time
    apariciones = {}
    vehiculos = {}
    llave = decimales(lat) + "_" + decimales(long)
    rappis = dg.get_vertex_information(catalog["grafo"], llave)["value"]
    for i in range(al.size(catalog["registros"])):
        if catalog["registros"]["elements"][i]["Restaurant_latitude"] == lat and catalog["registros"]["elements"][i]["Restaurant_longitude"] == long:
            if catalog["registros"]["elements"][i]["Delivery_person_ID"] in rappis:
                if catalog["registros"]["elements"][i]["Delivery_person_ID"] not in apariciones:
                    apariciones[catalog["registros"]["elements"][i]["Delivery_person_ID"]] = 1
                else:
                    apariciones[catalog["registros"]["elements"][i]["Delivery_person_ID"]] += 1
                if catalog["registros"]["elements"][i]["Delivery_person_ID"] not in vehiculos:
                    vehiculos[catalog["registros"]["elements"][i]["Delivery_person_ID"]] = al.new_list()
                    al.add_last(vehiculos[catalog["registros"]["elements"][i]["Delivery_person_ID"]], catalog["registros"]["elements"][i]["Type_of_vehicle"])
                else:
                    al.add_last(vehiculos[catalog["registros"]["elements"][i]["Delivery_person_ID"]], catalog["registros"]["elements"][i]["Type_of_vehicle"])
    if apariciones:
        rappi = max(apariciones, key=apariciones.get)
        delivery_count = apariciones[rappi]
        vehicles = vehiculos[rappi]
        contador_2 = {}
        for vehicle in vehicles:
            if vehicle not in contador_2:
                contador_2[vehicle] = 1
            else:
                contador_2[vehicle] += 1
        vehicle = max(contador_2, key=contador_2.get)
        preferencia_vehiculo = contador_2[vehicle]
    end_time = get_time()
    time = delta_time(start_time, end_time)
    return rappi, delivery_count, preferencia_vehiculo, time             
            


def req_4(catalog, punto_A, punto_B):
    """
    Retorna el resultado del requerimiento 4
    """
    start_time = get_time()
    
    graph = catalog["grafo"]
    
    bfs_result = bfs.bfs(graph, punto_A)
    
    path = bfs.path_to(bfs_result, punto_B)
    
    if not path:
        return 0.0, [], []
    
    secuencia_ubicaciones = al.new_list()
    domiciliarios_por_punto = al.new_list()
    
    for punto in path:
        al.add_last(secuencia_ubicaciones,(punto))
        vertex_info = dg.get_vertex_information(graph, punto)
        ids_en_punto = al.new_list()
        al.add_last(ids_en_punto,vertex_info["value"]["elements"])
        al.add_last(domiciliarios_por_punto,(ids_en_punto))

    domiciliarios_comunes = al.new_list()
    al.add_last(domiciliarios_comunes,domiciliarios_por_punto)
    
    end_time = get_time()
    time = delta_time(start_time, end_time)
    
    return time, secuencia_ubicaciones, domiciliarios_comunes


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def reconstruct_path(graph, visited, source, target):
    """
    Reconstruye el camino mínimo desde el vértice source al vértice target.
    """
    path = al.new_list()
    current = target
    al.add_last(path, source)
    while current != source:
        al.add_last(path, current)
        neighbors = dg.adjacents(graph, current)
        keys = mp.key_set(neighbors)
        size_keys = al.size(neighbors)
        centinela = False
        i = 0
        while not centinela and i < size_keys:
            edge = dg.get_edge(graph, keys["elements"][i], current)
            if mp.get(visited, keys["elements"][i]) + edge["weight"] == mp.get(visited, current):
                current = keys["elements"][i]
                centinela = True
            i += 1
        if not centinela:
            return None
    return path

def req_6(catalog, id):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = get_time()
    dijkstra_result = dij.dijkstra(catalog["grafo"], id)
    visited = dijkstra_result["visited"] 
    reachable = {}
    keys = mp.key_set(visited)
    for key in keys:
        if mp.get(visited, key) < float('inf'):
            reachable[key] = mp.get(visited, key)
    sorted_reachable = sorted(reachable.keys()) 
    max_vertex = max(reachable, key=reachable.get)
    max_cost = reachable[max_vertex]
    path = reconstruct_path(catalog["grafo"], visited, id, max_vertex)
    end_time = get_time()
    time = delta_time(start_time, end_time)

    return path, path["size"], sorted_reachable, path["elements"], max_cost, time



def req_7(catalog, punto_A, domiciliario_id):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start = get_time()
    grafo_original = catalog["grafo"]
    
    subgrafo = dg.new_graph(1000)
    vertices = grafo_original["vertices"]["table"]
    
    for entry in vertices:
        if entry is not None:
            id_nodo = entry["key"]
            lista_domiciliarios = entry["value"]
            if al.is_present(lista_domiciliarios, domiciliario_id):

                dg.insert_vertex(subgrafo, id_nodo, lista_domiciliarios)
    
    for entry in vertices:
        if entry is not None:
            u = entry["key"]
            if dg.contains_vertex(subgrafo, u):
                adyacentes = dg.adjacents(grafo_original, u)
                for i in range(1, al.size(adyacentes)+1):
                    v = al.get_element(adyacentes, i)
                    if dg.contains_vertex(subgrafo, v):
                        arco = dg.get_edge(grafo_original, u, v)
                        if not dg.contains_vertex(subgrafo, u, v):
                            dg.add_edge(subgrafo, u, v, arco["weight"])
    

    mst_result = prim.prim(subgrafo, punto_A)


    total_peso = 0
    ubicaciones = al.new_list()
    
    edges = mst_result["edges"]
    for i in range(1, al.size(edges)+1):
        edge = al.get_element(edges, i)
        total_peso += edge["weight"]
        if not al.is_present(ubicaciones, edge["vertexA"]):
            al.add_last(ubicaciones, edge["vertexA"])
        if not al.is_present(ubicaciones, edge["vertexB"]):
            al.add_last(ubicaciones, edge["vertexB"])

    ubicaciones_py = al.new_list()
    for i in range(1, al.size(ubicaciones)+1):
        al.add_last(ubicaciones_py,al.get_element(ubicaciones, i))
    al.merge_sort(ubicaciones_py)

    stop = get_time()
    tiempo_total = delta_time(start,stop)

    return {
        "tiempo_ejecucion": tiempo_total,
        "num_ubicaciones": al.size(ubicaciones_py),
        "ubicaciones": ubicaciones_py,
        "costo_total": round(total_peso, 2)
    }

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
