# *****
# *****
# *****
# *****
# *****

#square pattern
# def square_pattern(n):

#     for i in range(n):
#         print("*" * n)


# square_pattern(5)


# *
# **
# ***
# ****
# *****
#increasing Right Angled Triangle

# def right_angled_triangel_increasing(n):
#     for i in range(1, n + 1):
#         print('*' * i)

# right_angled_triangel_increasing(5)


# *****
# ****
# ***
# **
# *
# def right_angled_triangel_decreasing(n):
#     for i in range(n):
#         print('*' * (n - i))


# right_angled_triangel_decreasing(5)


#     *
#    **
#   ***
#  ****
# *****
# def right_aligned_triangle(n):
#     for i in range(1, n + 1):
#         print(' ' * (n -i) + '*' * i )

# right_aligned_triangle(5)


#pyramid


# def pyramid(n):
#     for i in range(1, n + 1):
#         print(" " * (n - i) + '*' * (2 * (i- 1) + 1))

# pyramid(5)

# def inverted_pyramid(n):
#     for i in range(1, n + 1):
#         print(' ' * i + '*' * (2 * (n - i) + 1))


# inverted_pyramid(5)


# def diamond(n):
#     for i in range(n):
#         print(' ' * (n - i -1 )+ '*' * ( 2 * i + 1))
#     for j in range(n - 2, -1 , -1):
#         print(' ' * (n - j -1 )+ '*' * ( 2 * j + 1) )

# diamond(5)


# def hour_glass(n):
#     for i in range(n) :
#         print(" " * i + "*" * (2 * (n - i) -  1))

#     for j in range(n - 2, - 1, -1):
#         print(" " * j + "*" * (2 * (n - j) - 1))


# hour_glass(5)


#pascals triangle

# def centrealigned_pascals_triangle(n):
#     triangle = []
#     for row in range(n):
#         new_row = [1]
#         if row > 0:
#             for col in range(1, row):
#                 new_row.append(triangle[row-1][col-1] + triangle[row-1][col])
#             new_row.append(1)
#         triangle.append(new_row)

#     for i in range(n):
#         print(" " * (n - i), end=" ")

#         for num in triangle[i]:
#             print(f"{num}", end=" ")
#         print()


# centrealigned_pascals_triangle(2)



# 1
# 5 1
# 8 4 1
# 10 6 3 1
# 11 7 4 2 1

# def number_triangle(n):
#     m = n - 1
#     first_num = 1
#     rows = []
#     rows.append([first_num])

#     for r in range(2, n + 1):
#         first_num +=  m - (r - 2)
#         row = [first_num]
#         for  j in range(2, r+1):
#             row.append(row[-1] - (m - (j - 2)))
#         rows.append(row)

#     return rows

# for row in number_triangle(5):
#     print(" ".join(map(str, row)))



def floyds_triangle(n):
    count = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(count, end=" ")
            count += 1
        print()


floyds_triangle(5)


def palindromic_triangle(n):
    for row in range(1, n + 1):
        print(" " * (n - row), end="")               
        
        for j in range(1, row+ 1):
            print(j, end="")
        for i in range(row - 1, 0, -1):
            print(i, end="")
        print()
