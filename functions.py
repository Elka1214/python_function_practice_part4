def max_num(a, b, c):
    return max([a, b, c])


print(max_num(1, 2, 3))
print(max_num(4, 5, 6))
print(max_num(7, 8, 9))


def mult_list(lst):
    if len(lst) == 0:
        return 0
    prod = lst[0]
    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i
    return prod


print(mult_list([1, 2, 3]))
print(mult_list([]))
print(mult_list([15]))
