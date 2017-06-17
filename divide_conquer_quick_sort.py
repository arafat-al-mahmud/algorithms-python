
#takes O(n^2) time
def quick_sort_slower(array):

    if(len(array) < 2):
        return array

    pivot = array[0]

    pivot_left_array = [i for i in array[1:] if i<= pivot]
    pivot_right_array = [i for i in array[1:] if i> pivot]

    return quick_sort_slower(pivot_left_array) + [pivot] + quick_sort_slower(pivot_right_array)


print(quick_sort_slower([2,4,1,5,7,0]))  #[0, 1, 2, 4, 5, 7]

#takes O(nlogn) time
def quick_sort_faster(array):

    if(len(array)<2):
        return array

    pivot_index = len(array) // 2

    pivot = array[pivot_index]

    pivot_left_array = [i for i in array[:pivot_index] if i<=pivot]
    pivot_left_array = pivot_left_array + [i for i in array[pivot_index+1:] if i<= pivot]

    pivot_right_array = [i for i in array[:pivot_index] if i> pivot]
    pivot_right_array = pivot_right_array + [i for i in array[pivot_index+1:] if i> pivot]

    return quick_sort_faster(pivot_left_array) + [pivot] + quick_sort_faster(pivot_right_array)

print(quick_sort_faster([-1, 4, 5, 3, 2, -4])) #[-4, -1, 2, 3, 4, 5]