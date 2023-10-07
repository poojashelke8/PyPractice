def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        min_ele = i
        for j in range(min_ele+1,size):
            if arr[min_ele] > arr[j]:
                min_ele = j
        arr[i],arr[min_ele] = arr[min_ele],arr[i]




if __name__ == "__main__":
    elements = [6, 3, 9, 5, 1]

    selection_sort(elements)
    print(elements)