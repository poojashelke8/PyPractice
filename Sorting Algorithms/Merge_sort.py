def merge_sort(ele):
    if len(ele) <= 1:
        return ele
    
    mid = len(ele)//2
    left = ele[:mid]
    right = ele[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_sorted_list(left,right,ele)

def merge_sorted_list(left,right,ele):
    len_left = len(left)
    len_right = len(right)
    i = j = k = 0
    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            ele[k] = left[i]
            i+=1
        else:
            ele[k] = right[j]
            j+=1
        k+=1
    
    while i <len(left):
        ele[k] = left[i]
        i+=1
        k+=1
    while j <len(right):
        ele[k] = right[j]
        j+=1
        k+=1

if __name__ == "__main__":
    elements = [6, 3, 9, 5, 1]

    merge_sort(elements)
    print(elements)