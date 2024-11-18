def mergesort(list_of_items):

    if len(list_of_items) < 2:
        return list_of_items
    
    left_list = list_of_items[:len(list_of_items) // 2]
    right_list = list_of_items[len(list_of_items) // 2:]
                       
    left_list = mergesort(left_list)
    right_list = mergesort(right_list)
    return merge(left_list, right_list)

def merge(left_list, right_list):
    result_list = []

    while left_list and right_list:
        if left_list[0] < right_list[0]:
            result_list.append(left_list[0])
            left_list.pop(0)
        else:
            result_list.append(right_list[0])
            right_list.pop(0)

    if left_list:
        result_list.extend(left_list)
    else:
        result_list.extend(right_list)

    return result_list




list_test = ["a", "g", "i", "d", "b", "z", "r", "h", "c"]
#list_test = [94, 35, 98, 65, 63, 12, 51, 81, 77, 64]

new_list = mergesort(list_test)

for item in new_list:
    print(item, end= ", ")

