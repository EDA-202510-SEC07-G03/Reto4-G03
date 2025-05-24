from DataStructures.List import array_list as lt

def new_queue():
    return lt.new_list()

def peek(my_queue):
    first = lt.first_element(my_queue)
    return first

def is_empty(my_queue):
    return  lt.is_empty(my_queue)


def dequeue(my_queue):
    return lt.remove_first(my_queue)


def size(my_queue):
    return lt.size(my_queue)



def enqueue(my_queue,element):
    
    nueva_cola=lt.add_last(my_queue,element)
    return nueva_cola