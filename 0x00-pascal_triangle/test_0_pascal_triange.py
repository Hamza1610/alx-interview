#!/usr/bin/python3

import pascal_triangle
''' A function that test how the pascal triangle works '''
def test_pascal_triangle():
    ''' Checks the value returned through calling the pacscal_triangle function '''

    list_triangle_nums = pascal_triangle.pascal_triangle(10)
    for item in list_triangle_nums:
        print(item)

test_pascal_triangle()