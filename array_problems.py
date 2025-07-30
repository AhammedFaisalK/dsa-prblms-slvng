# def find_largest(arr):
#     if not arr:
#         return 
#     max_val = arr[0]
#     for num in arr:
#         if num > max_val:
#             max_val = num
#     return max_val

# arr = [5, 9, 26, 78,10]
# print(find_largest(arr))

# def second_largest_element(arr):
#     if len(arr) < 2:
#         return "There is no second largest element"
        
#     first = second = float("-inf")
    
#     for num in arr:
#         if num > first:
#             second = first
#             first = num
#         elif first > num > second:
#             second = num
#     return second if second != float('-inf') else "There is no second largest element"
    
    
# arr = [3]
# print(second_largest_element(arr))

# #check array is sorted
# def is_sorted(arr):
#     if not arr:
#         return False
#     for i in range(len(arr) - 1):
#         if arr[i] > arr[i + 1]:
#             return False
#     return True

# arr = [3, 5, 32, 33, 4]
# print(is_sorted(arr))


#remove duplicates from sorted array

# def remove_duplicates(arr):
#     if not arr:
#         return 0
#     i = 0
#     for j in range(1, len(arr)):
#         if arr[j] != arr[i]:
#             i += 1
#             arr[i] = arr[j]
#     return i + 1
    

# arr = [2, 5, 8, 23, 23,  54, 65]

# length = remove_duplicates(arr)
# print(arr[:length])
            
# #Left Rotate an array by one place
# def array_rotate_one_by_place(arr):
#     if not arr:
#         return 
#     first = arr[0]
#     for i in range(1, len(arr)):
#         arr[i - 1] = arr[i]
#     arr[-1] = first
    
#     return arr
    
# arr = [12, 54, 32, 3, 6, 8]
# array_rotate_one_by_place(arr)

# print(arr,"Rotated one place")

#k roatation of an array

# def reverse_elements(arr, start, end):
#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1
# def array_of_k_rotation(arr, k):
#     if not arr:
#         return 

#     n = len(arr)
#     k %= n
    
#     reverse_elements(arr, 0 , k - 1)
    
#     reverse_elements(arr, k, n - 1)
    
#     reverse_elements(arr, 0, n - 1)
#     return arr

    
# arr = [12, 54, 32, 3, 6, 8]
# array_of_k_rotation(arr, k=3)
  
# print(arr)

#move zero to end

# def move_zero_to_end(arr):
#     z = 0
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[i], arr[z] = arr[z], arr[i]
#             z += 1
#     return arr
    
# arr = [23, 56, 0, 1, 2, 4, 0, 9] 

# print(move_zero_to_end(arr))



#linear search
# def linear_search(arr, num):
#     for i in range(len(arr)):
#         if arr[i] == num:
#             return i
#     return  False

# arr = [2, 45, 5, 6, 32]
# num = 10
# print(linear_search(arr, num))

#Find union

# def find_union(arr1, arr2):
#     union_set = set(arr1 + arr2)
#     return list(union_set)

# arr1 = [23, 4, 1,3, 4, 6, 7]
# arr2= [45, 6, 3, 22]
# print(find_union(arr1, arr2))



#consective ones


# def consective_ones(arr):
#     max_count = 0
#     current = 0
#     for num in arr:
#         if num == 1:
#             current +=1
#             max_count = max(max_count, current)
#         else:
#             current = 0
#     return max_count

# arr = [0, 1, 0, 1, 0, 0, 1, 1]
# print(consective_ones(arr))

#Find the number that appears once, and other numbers twice.

# def find_single_number(arr):
#     result = 0
#     for num in arr:
#         result ^= num
    
#     return result

# arr = [2, 3, 2, 3, 1, 5, 5]
# print(find_single_number(arr))
    
#Find the longest sub array

# def longest_subarray_sum_k(arr, k):
#     left = 0
#     current_sum = 0
#     max_length = 0
    
#     for right in range(len(arr)):
#         current_sum += arr[right]
        
#         while current_sum > k and left <= right:
#             current_sum -= arr[left]
#             left += 1
            
#         if current_sum == k:
#             max_length = max(max_length, right - left + 1)
            
#     return max_length
            
            
# arr = [1, 3, 5, 8, 2, 1, 3]
# k = 5

# print(longest_subarray_sum_k(arr, k))
        
#finding the longest subarray with sum K (works with both positive and negative numbers).
def longest_subarray_with_sum_k(arr, k):
    prefix_sum_map = {}
    prefix_sum = 0
    max_length = 0
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum == k:
            max_length = i + 1
        
        if prefix_sum in prefix_sum_map:
            max_length = max(max_length, i - prefix_sum_map[prefix_sum- k] )
        if prefix_sum not in prefix_sum_map:
            prefix_sum_map[prefix_sum] = i
            
    return max_length


arr = [1, -1, 5, -2, 3]
k = 3

print(longest_subarray_with_sum_k(arr, k))