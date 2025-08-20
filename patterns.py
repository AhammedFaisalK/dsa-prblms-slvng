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



# def floyds_triangle(n):
#     count = 1
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print(count, end=" ")
#             count += 1
#         print()


# floyds_triangle(5)


# def palindromic_triangle(n):
#     for row in range(1, n + 1):
#         print(" " * (n - row), end="")               
        
#         for j in range(1, row+ 1):
#             print(j, end="")
#         for i in range(row - 1, 0, -1):
#             print(i, end="")
#         print()


# def mirror_number_pyramid(n):
#     for row in range(1, n+1):
#         print(" " * (n -row) + f"{row} "* row)
    
# mirror_number_pyramid(5)

# def butterfly_pattern(n):
#     for i in range(1, n + 1):
#         print("*" * i + " " * (2 * ( n - i ))+ "*" * i)
#     for j in range(n -1, -1, -1):
#         print("*" * j + " " * (2 * (n - j) )+ "*" * j)

# butterfly_pattern(4)

# def zig_zag(r, c):
#     if r <=0  or  c <= 0 :
#         return
#     cycle = 2 * (r - 1) if r > 1 else 1
#     for row in range(r):
#         for col in range(c):
#             if col % cycle == row or col % cycle == cycle - row :
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()


# zig_zag(3, 9)


# def sandglass(n):
#     for row in range(n):
#         print(" " * row  + "*" * (2  *( n - row ) - 1) )

#     for j in range(n - 2, -1 , -1 ):
#         print(" " * j  + "*" * (2  *( n - j ) - 1) )



# sandglass(5)


# def numeric_hollow_pyramid(n):
#     if n <= 0:
#         return
#     for i in range(1, n + 1):
#         line = " " * ( n - i)
#         if i == 1:
#             line += "1"
#         elif i < n:
#             spaces = 2 * i -3
#             line +=  "1" + " " * spaces + str(i)
#         else:
#             line += " ".join(str(x) for x in range(1, n + 1))
#         print(line)

# numeric_hollow_pyramid(5)


# def full_numeric_pyramid(n):
#     for i in range(1,n + 1):
#         print(" " * (n - i), end="")
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()

# full_numeric_pyramid(5)


# def inverted_numeric_pyramid(n):
#     for i in range(n, -1 , -1):
#         print(" " * (n -i), end="")
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()

# inverted_numeric_pyramid(5)


# def inverted_hollow_pyramid(n):
#     for i in range(n, 0, -1):
#         if i == n:
#             print(" ".join(str(x) for x in range(1, n +1)))
#         elif i == 1:
#             print(" " * (n - 1) + "1")
#         else:
#             outside_space = " " * (n - i)
#             inside_space = " " * (2 * i - 3)
#             print(outside_space + "1" + inside_space + str(i))

# inverted_hollow_pyramid(5)


# Centered Numeric Diamond


# def centered_numeric_diamond(n):
#     for i in range(1, n+1):
#         print(" " * (n - i), end="")
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()
#     for i in range(n - 1, 0, -1):
#         print(" " * (n - i), end="")
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()

# centered_numeric_diamond(5)


# Hollow Numeric Diamond
# def hollow_numeric_diamond(n):
#     for i in range(1, n + 1):
#         if i == 1:
#             print(" " * (n - i) + "1")
#         else:
#             print(" " * (n -i ) + "1" + " " * (2 * i - 3) + str(i))
#     for j in range(n -1, 0, -1):
#         if j == 1:
#             print(" " * (n - j) + "1")
#         else:
#             print(" " * (n -j ) + "1" + " " * (2 * j - 3) + str(j))



# hollow_numeric_diamond(5)

# Hollow Square / Hollow Rectangle Pattern

# def hollow_square_(n):
#     for i in range(n):
#         for j in range(n):
#             if i == 0 or i == n-1 or j == 0 or j == n-1:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()

# hollow_square_(5)


def hollow_rect_pattern(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows-1 or j == 0 or j == cols - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

hollow_rect_pattern(4, 10)
