import math

def count_digits(num):
    if num == 0:
        return 1
    count = 0
    while num > 0:
        num  = num // 10
        count += 1
    return count

data = 235
print(count_digits(data))

# def reverse_number(num):
#     reverse = 0
#     while num > 0:
#         last_digit = num % 10
#         num = num // 10
#         reverse = reverse * 10 + last_digit
#     return reverse

# number = 97489
# print(reverse_number(number))

# def check_palindrome(num):
#     if num == reverse_number(num):
#         return True
#     else:
#         return False
    
# numbes = 121
# print(check_palindrome(numbes))

def arm_strong_numbers(num):
    orginal = num
    n = len(str(num))
    results = 0
    while num > 0:
        digit = num % 10
        results += digit **n 
        num = num //10
    return results == orginal

test = 121
print(arm_strong_numbers(test))


# def print_all_divisors(n):
#     for i in range(1, ):
#         if n % i == 0:
#             print(i, end=" ")
#     print()


# print_all_divisors(35)


def print_dvisors(n):
    divisors = set()
    limit = int(math.sqrt(n))
    for i in  range(1, limit + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

print(print_dvisors(34))



def is_prime(n):
    if n <= 1:
        return False
    
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            if (n // i) != i:   # avoid double counting square roots
                count += 1
    
    return count == 2


# Example usage
print(is_prime(37))  # True
print(is_prime(36))  # False


#efficient method
def is_prime(n):
    if n <= 1: 
        return False
    if n <= 3: 
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

print(is_prime(5))
