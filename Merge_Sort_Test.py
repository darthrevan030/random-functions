def mergesort(list_of_items):

    if len(list_of_items) < 2:
        return list_of_items
    left_list = list_of_items[:len(list_of_items) // 2]
    right_list = list_of_items[len(list_of_items) // 2]
                       
    left_list = mergesort(left_list)
    right_list = mergesort(right_list)
    return sort_two_list(left_list, right_list)

def sort_two_list(list_1, list_2):
    final_list = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            final_list.append(list_1[i])
            i += 1
            continue
        final_list.append(list_2[j])
        j += 1

    while i < len(list_1):
        final_list.append(list_1[i])
        i = i + 1

    while j < len(list_2):
        final_list.append(list_2[j])
        j = j + 1

    return final_list


my_list = [3, 8, 2, 7, 1, 4, 5]
ans = mergesort(my_list)
print(ans)