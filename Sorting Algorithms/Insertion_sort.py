def insertion_sort(ele):
    for i in range(1,len(ele)):
        anchor = ele[i]
        j = i-1
        while j>=0 and anchor <ele[j]:
            ele[j+1] = ele[j]
            j = j -1
        ele[j+1] = anchor

if __name__ == "__main__":
    elements = [1,5,3,9,6]

    insertion_sort(elements)
    print(elements)