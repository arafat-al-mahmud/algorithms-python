def recursive_add(array):

    if(len(array) == 0):
        return 0

    return array[0] + recursive_add(array[1:])

print(recursive_add([1,2,3,4,5,0,-1])) #14