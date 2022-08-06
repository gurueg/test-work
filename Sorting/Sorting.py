import random


"""
Функция быстрой сортировки
Средняя сложность и время выполнения O(n log n)
"""
def QuiqSort(sorting_list):

    if len(sorting_list) < 1:
        return sorting_list

    center_idx = random.randint(0, len(sorting_list)-1)
    center = sorting_list[center_idx]

    left_list = []
    right_list = []

    for idx, value in enumerate(sorting_list):
        if center_idx != idx:
            if value < center:
                left_list.append(value)
            else:
                right_list.append(value)

    result = QuiqSort(left_list)
    result.append(center)
    result += QuiqSort(right_list)
    return result


if __name__ == "__main__":
    pass
    