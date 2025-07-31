def find_element_index(tup, elem):
    """
    Searches for an element in a tuple and returns its index.
    
    Parameters:
    tup (tuple): The tuple to search in.
    elem: The element to search for.
    
    Returns:
    int: The index of the element if found, otherwise -1.
    """
    for i in range(len(tup)):
        if tup[i] == elem:
            return i
    return -1

# Example usage
tup = (10, 20, 30, 40, 50)
elem =int(input())
print(tup, elem)  # Output: 2


