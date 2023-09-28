def swap(a,b,ele):
    if a != b:
        temp = ele[a]
        ele[a]= ele[b]
        ele[b] = temp

def partition(ele,start,end):
    pivot_index = start
    pivot = ele[pivot_index]

    while start < end:
        while start <len(ele) and ele[start] <= pivot:
            start+=1

        while ele[end] > pivot:
            end-=1

        if start<end:
            swap(start,end,ele)

    swap(pivot_index,end,ele)
    return end
    

def quick_sort(ele,start,end):
    if start<end:
        pi = partition(ele,start,end)
        quick_sort(ele,start,pi-1)
        quick_sort(ele,pi+1,end)
        
    

if __name__ == "__main__":
    elements = [1,5,3,9,6]

    quick_sort(elements,0,len(elements)-1)
    print(elements)


