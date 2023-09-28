def bubble_sort(ele,key=None):
    size = len(ele)
    swapped = False
    for i in range(size-1):
        for j in range(size-1-i):
            a = ele[j][key]
            b=ele[j+1][key]
            if a >b:
                temp = ele[j]
                ele[j] = ele[j+1]
                ele[j+1] = temp
                swapped=True
        if not swapped:
            break

if __name__ == "__main__":
    # elements = [1,6,4,2,9]
    # elements = [1,2,3]
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    bubble_sort(elements,key="transaction_amount")
    print(elements)
    