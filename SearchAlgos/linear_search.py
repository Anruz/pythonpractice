def linear_search(list,key):
    '''
    Searches for an element in the list in a linear order, from start to end of the list
    Complexity will be O(n)
    :param list: List of elements in which the element need to be searched
    :param key: Element to be found
    '''
    for i in range(len(list)):
        if list[i] == key:
            print(f"Element found at index {i}")
        else:
            print(f"Element not found")

linear_search([1,2,3,4,5,6,7,8,9],8)