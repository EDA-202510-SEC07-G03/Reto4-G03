from DataStructures.List import array_list as al
from DataStructures.Priority_queue import index_pq_entry as pqe

def default_compare_higher_value(father_node, child_node):
    if pqe.get_key(father_node) >= pqe.get_key(child_node):
        return True
    return False

def default_compare_lower_value(father_node, child_node):
    if pqe.get_key(father_node) <= pqe.get_key(child_node):
        return True
    return False

def new_heap(is_min_pq = True):
    if is_min_pq:
        compare = default_compare_lower_value
    else:
        compare = default_compare_higher_value
    elements = al.new_list()
    al.add_last(elements, None)
    return {
        "elements": elements,
        "size": 0,
        "cmp_function": compare,
    }

def size(my_heap):
    return my_heap["size"]

def priority(my_heap, parent, child):
    cmp = my_heap["cmp_function"](parent, child)
    if cmp > 0:
        return True
    return False

def swim(my_heap, pos):
    elements = my_heap["elements"]["elements"]
    proceed = True
    while proceed and pos > 1:
        parent_pos = pos // 2
        parent = elements[parent_pos]
        child = elements[pos]
        if priority(my_heap, parent, child):
            al.exchange(my_heap["elements"], parent_pos, pos)
            pos = parent_pos
        else:
            proceed = False
    return my_heap

def sink(my_heap, pos):
    elements = my_heap["elements"]["elements"]
    proceed = True
    while proceed and pos * 2 <= my_heap["size"]:
        l_child_pos = pos * 2
        l_child = elements[l_child_pos]
        r_child_pos = pos * 2 + 1
        if r_child_pos <= my_heap["size"]:
            r_child = elements[r_child_pos]
        child_pos = l_child_pos 
        if r_child:
            if priority(my_heap, l_child, r_child):
                child_pos = r_child_pos
        father = elements[pos]
        child = elements[child_pos]
        if priority(my_heap, father, child):
            proceed = False
        else:
            al.exchange(my_heap["elements"], pos, child_pos)
            pos = child_pos
    return my_heap
            
def insert(my_heap, value, key):
    node = pqe.new_pq_entry(value, key)
    al.add_last(my_heap["elements"], node)
    my_heap["size"] += 1
    return swim(my_heap, my_heap["size"])

def remove(my_heap):
    if is_empty(my_heap):
        return None
    node = my_heap["elements"]["elements"][1]
    al.exchange(my_heap["elements"], 1, my_heap["size"])
    al.remove_last(my_heap["elements"])
    my_heap["size"] -= 1
    if not is_empty(my_heap):
        my_heap = sink(my_heap, 1)
    return pqe.get_index(node)
    

def is_empty(my_heap):
    if my_heap["size"] == 0:
        return True
    return False

def get_first_priority(my_heap):
    if is_empty(my_heap):
        return None
    first = my_heap["elements"]["elements"][1]
    value = pqe.get_index(first)
    return value

def del_min(my_heap):

    if is_empty(my_heap):
        return None

    elements = my_heap["elements"]["elements"]
    min_node = elements[1]

    # Reorganizar heap
    al.exchange(my_heap["elements"], 1, my_heap["size"])
    al.remove_last(my_heap["elements"])
    my_heap["size"] -= 1

    if not is_empty(my_heap):
        sink(my_heap, 1)

    return {
        "key": pqe.get_index(min_node),
        "priority": pqe.get_key(min_node)
    }