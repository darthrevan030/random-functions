def merge_sort(my_list):

    # Base Case
    if len(my_list) <= 1:
        return my_list

    list_1 = my_list[0:len(my_list) // 2]
    list_2 = my_list[len(my_list) // 2:]

       # Induction Step
    ans_1 = merge_sort(list_1)
    ans_2 = merge_sort(list_2)

    # Sorting and merging two sorted list
    sort_list = merge(ans_1, ans_2)
    return sort_list

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


my_list = [3, 8, 2, 7, 1, 4, 5]
ans = merge_sort(my_list)
print(ans)
