# def print_n_times(n):
#     if n <=0 :
#         return 
#     print("HEllo")
#     return print_n_times(n - 1)

# print_n_times(5)


# def print_1_to_n(n, current=1):
#     if n <= 0:
#         return
#     print(current)
#     return print_1_to_n(n - 1, current + 1)

# print_1_to_n(10)


# def print_n_to_1(n):
#     if n <= 0:
#         return 
#     print(n)
#     return print_n_to_1(n - 1)

# print_n_to_1(10)

def print_sum_n_numbers(n, sum=0):
    if n < 1:
        return sum
    sum += n
    return print_sum_n_numbers(n - 1, sum)

print(print_sum_n_numbers(5))


def factorial_number(n):
    if n == 0:
        return 1
    return n * factorial_number(n - 1)


print(factorial_number(5))


def reverse_an_array(arr, start, end):
    if start >= end:
        return 
    arr[start], arr[end] = arr[end] , arr[start]
    reverse_an_array(arr, start+1, end - 1)

arr = [2, 4, 3, 21, 55, 33, 20]
start = 0
end = len(arr) - 1
reverse_an_array(arr, start, end)
print(arr)
