"""
Task

There is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format

The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

Output Format

Print the amount of money earned by .

Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200
Explanation

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned =  55 + 45 + 40 + 60 = 200
"""

no_shoe = int(input())
shoe_sizes = input().split(" ")
no_cust = int(input())
total = 0
for i in range(no_cust):
    data = input().split(" ")
    if data[0] in shoe_sizes:
        shoe_sizes.remove(data[0])
        total += int(data[1])
print(total)

print("------------------------------------------------------------------")

"""
A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either side of the deque
with approximately the same  performance in either direction.


Task

Perform append, pop, popleft and appendleft methods on an empty deque .

Input Format

The first line contains an integer , the number of operations.
The next  lines contains the space separated names of methods and their values.

Output Format

Print the space separated elements of deque .

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output

1 2
"""

from collections import deque

d = deque()

operations = int(input())

for i in range(operations):
    data = list(map(str,input().split()))
    if data[0] == "append":
        d.append(int(data[1]))
    elif data[0] == "appendleft":
        d.appendleft(int(data[1]))
    elif data[0] == "pop":
        d.pop()
    elif data[0] == "popleft":
        d.popleft()
print(*d)





