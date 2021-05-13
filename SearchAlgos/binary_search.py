def binary_search(input_list,ele):
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
