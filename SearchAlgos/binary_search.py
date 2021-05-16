def binary_search(input_list,ele):
    '''
    Finds an element from a given list by splitting the lists into sublists
    Each iteration discards half of the list.
    Complexity will be O(log n)
    :param input_list: List of elements as input
    :param ele: Element to be searched
    :return: Element found; -1 in the case of element not found
    '''
    min = 0
    max = len(input_list)
    mid = 0

    while min < max:
        mid = (min+max)//2
        if input_list[mid] > ele:
            min = mid + 1
        elif input_list[mid] < ele:
            max = mid -1
        else:
            return mid
        return -1

val = binary_search([1,2,3,4,5], 3)
print(val)
