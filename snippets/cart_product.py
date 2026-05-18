
def cartesian_product(list_of_lists):
    """
    Cartesian product of a list of lists - completed without using itertools or list comprehensions
    """
    if not list_of_lists:
        return [[]]

    result = []
    first_list = list_of_lists[0]
    rest_product = cartesian_product(list_of_lists[1:])

    for item in first_list:
        for product in rest_product:
            result.append([item] + product)

    return result


print(cartesian_product([["1", "2", "3"], ["4", "5", "6"]]))

print(cartesian_product([["1", "2"], ["3", "4"], ["5", "6"]]))