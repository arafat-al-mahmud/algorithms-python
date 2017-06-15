def recursive_max_item_in_list(list):

    if(len(list) == 1):
        return list[0]

    max_rest = recursive_max_item_in_list(list[1:])

    if list[0] >= max_rest :
        return list[0]
    else :
        return max_rest

print(recursive_max_item_in_list([2,5,9,0,-1])) #9