
def binary_search(array, low, high, item):

    if(low>high) :
        return -1

    mid = (low + high)//2

    if(item == array[mid]):
        return mid
    elif item < array[mid]:
        return binary_search(array, low, mid-1, item)
    elif item > array[mid]:
        return binary_search(array, mid+1, high, item)


print ( binary_search([1,4,5,7], 0, 3, 5)) #2
print ( binary_search([1,4,5,7], 0, 3, 10)) #-1
