def iterative_binary_search(array, item):

    low = 0
    high = len(array) - 1

    while(low<=high):

        mid = (low+high)//2

        if (item == array[mid]):
            return mid
        elif item < array[mid]:
            high = mid - 1
        elif item > array[mid]:
            low = mid + 1

    return -1

print ( iterative_binary_search([1,4,5,7], 5)) #2
print ( iterative_binary_search([1,4,5,7], 10)) #-1
