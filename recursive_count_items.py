def recursive_count_items(list):

    if(len(list) == 0):
        return 0

    return 1 + recursive_count_items(list[1:])

print(recursive_count_items([1,2,4,5,0,-1, 3])) #7
