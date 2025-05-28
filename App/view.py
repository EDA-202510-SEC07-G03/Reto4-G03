import sys
import os
from tabulate import tabulate
import pprint as pp
import App.logic as log
data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Data')
default_name = os.path.join(data_dir, 'deliverytime_min.csv')

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    catalog = log.new_logic()
    return catalog

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    data = log.load_data(control, default_name)
    verticies = log.diagraph(control)
    edges = log.conexion_domicilios(control)
    print("Un total de: "+ str(data[0]) + " registros han sido cargados")
    print("Un total de: "+ str(data[1]) + " domiciliarios han sido encontrados")
    print("Un total de: "+ str(data[2]) + " restaurantes han sido encontrados")
    print("Un total de: "+ str(data[3]) + " domicilios han sido encontrados")
    print("El tiempo promedio de entrega es: " + str(data[4]) + " minutos")
    print("El grafo tiene un total de: " + str(verticies) + " vertices")
    print("El grafo tiene un total de: " + str(edges) + " arcos")


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    id_a = input("Ingrese el ID de la ubicacion de origen: ")
    id_b = input("Ingrese el ID de la ubicacion de destino: ")
    result = log.req_1(control, id_a, id_b)
    if result[0] is None:
        print("No hay un camino entre los puntos seleccionados")
    else:
        print("En el camino, se encontraron ")+str(result[1])+(" puntos intermedios")
        print("Listado de ID's de los domiciliarios encontrados: ")
        pp.pp(result[0])
        print("El camino encontrado es:")
        pp.pp(result[2])
        print("En el camino se encontraron los sigyientes restaurantes: ")
        pp.pp(result[3])
        print("El tiempo de ejecucion fue de "+str(result[4])+" ms")       
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    id = input("Ingrese el ID que desea analizar: ")
    result = log.req_3(control, id)
    if result[0] is None:
        print("No se encontro el ID solicitado en el registro")
    else:
        print("El ID del rappi que mas aparecio para el ID dado es: ")+str(result[0])
        print("El rappi aparecio un total de: ")+str(result[1])+(" veces")
        print("El vehiculo de preferencia del rappi es: ")+str(result[2])
        print("El tiempo de ejecucion fue de "+str(result[3])+" ms")


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    id_origen = input("Ingrese el ID del punto de origen: ")
    id_destino = input("Ingrese el ID del punto de destino: ")
    result = log.req_4(control, id_origen, id_destino)

    if result[0] is None or len(result[0]) == 0:
        print("No se encontraron domiciliarios en común entre las ubicaciones.")
    else:
        print("Los domiciliarios en común entre los dos puntos son:")
        pp.pp(result[0])
        print("La ruta entre las ubicaciones tiene " + str(result[1]) + " puntos intermedios.")
        print("El camino más corto es:")
        pp.pp(result[2])
        print("El tiempo de ejecución fue de " + str(result[3]) + " ms.")


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    id = input("Ingrese el ID que desea analizar: ")
    result = log.req_6(control, id)
    if result[0] is None:
        print("No se encontro un camino para el ID solicitado en el registro")
    else:
        print("El camino de costo minimo cuneta con ")+str(result[1])+(" puntos intermedios")
        print("El camino encontrado es:")
        pp.pp(result[2])
        print("el sub-camino que implico mayor costo es: ")
        pp.pp(result[3])
        print("El costo total del camino es: ")+str(result[4])
        print("El tiempo de ejecucion fue de "+str(result[5])+" ms")


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    
    punto_inicial = input("Ingrese el ID del punto geográfico inicial (ej. 4.6743_-74.0934): ")
    id_domiciliario = input("Ingrese el ID del domiciliario: ")
    result = log.req_7(control, punto_inicial, id_domiciliario)

    if result is None or len(result["ubicaciones"]) == 0:
        print("No se pudo construir una subred para el domiciliario dado desde el punto inicial.")
    else:
        print("Tiempo de ejecución: " + str(result["tiempo_ejecucion"]) + " ms")
        print("Cantidad de ubicaciones en la subred: " + str(result["num_ubicaciones"]))
        print("Identificadores de las ubicaciones ordenados alfabéticamente:")
        pp.pp(result["ubicaciones"])
        print("Costo total del Árbol de Recubrimiento Mínimo (en tiempo): " + str(result["costo_total"]))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
