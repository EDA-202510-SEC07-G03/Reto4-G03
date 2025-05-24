from DataStructures.List import single_linked_list as lt
from DataStructures.List import list_node as ln
def new_stack():
    return lt.new_list()

def push(my_stack,element):
    """
    Añade un elemento al final de la estructura de datos
    """
    new_node=ln.new_single_node(element)
    my_stack["last"]=new_node
    
    if my_stack["size"]==0:
        my_stack["first"]=new_node
    
    my_stack["size"]+=1
    
    return my_stack


def pop(my_stack):
    to_delete = my_stack["last"]
    reference = my_stack["first"]
    for i in range(0, (my_stack["size"])-2):
        reference = reference["next"]
        
    my_stack["last"] = reference
    
    my_stack["size"] -= 1
    return to_delete["info"]

def is_empty(my_stack):
    return lt.is_empty(my_stack)

def top(my_stack):
    return my_stack["last"]["info"]

def size(my_stack):
    return my_stack["size"]