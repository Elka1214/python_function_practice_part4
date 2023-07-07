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


def rev_string(string):
    return string[::-1]


# Test the function
my_string = input("Enter a string: ")
result = rev_string(my_string)
print(f"The reversed string is: {result}")


def num_within(num, start, end):
    return start <= num <= end


# Test the function with example cases
print(num_within(3, 2, 4))    # Returns True
print(num_within(3, 1, 3))    # Returns True
print(num_within(10, 2, 5))   # Returns False


def pascal(n):
    triangle = []

    for row in range(n):
        current_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)
            else:
                value = triangle[row - 1][col - 1] + triangle[row - 1][col]
                current_row.append(value)
        triangle.append(current_row)

    # Print Pascal's triangle
    for row in triangle:
        print(' '.join(map(str, row)))


def pascal_print(num_rows):
    pascal(num_rows)
    print()


# Test the function
pascal_print(1)
pascal_print(5)
