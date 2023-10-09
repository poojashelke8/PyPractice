def binary_search(numbers_list, number_to_find):
    left = 0
    right = len(numbers_list)-1
    mid = 0

    while left <= right:
        mid = (left+right)//2
        mid_num = numbers_list[mid]

        if mid_num == number_to_find:
            return mid
        
        if mid_num < number_to_find:
            left = mid +1
        else:
            right = mid  - 1
    return -1

def binary_recursive(numbers_list, number_to_find, left_indx, right_indx):
    if right_indx < left_indx:
        return -1
    
    mid = (left_indx+right_indx)//2
    mid_num = numbers_list[mid]

    if mid >= len(numbers_list) or mid < 0:
        return -1
    
    if mid_num == number_to_find:
            return mid
        
    if mid_num < number_to_find:
        left_indx = mid +1
    else:
        right_indx = mid  - 1

    return binary_recursive(numbers_list, number_to_find, left_indx, right_indx)





if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 21

    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")


    index = binary_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Number found at index {index} using binary search recursive")