
def find_smallest_element_index(array):

    smallest_elem_index, smallest_elem = 0, array[0]

    for index in range(1,len(array)):
        if(smallest_elem >= array[index]):
            smallest_elem_index = index

    return smallest_elem_index

#changes the original array and puts the elements in sorted order (ascending)
def selection_sort(array):

    sorted_array = []
    for i in range(len(array)):
        smallest_elem_index = find_smallest_element_index(array)
        sorted_array.append(array.pop(smallest_elem_index))

    return sorted_array

print(selection_sort([-1,2,0,-3,6]))

