def find_max_num(list_numbers):
    max_num = list_numbers[0]
    for number in list_numbers:
        if number > max_num:
            max_num = number
    return max_num


def weight_kg_to_lbs(weight):
    return weight / 0.45


def weight_lbs_to_kg(weight):
    return weight * 0.45
