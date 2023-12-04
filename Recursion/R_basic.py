def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
    
# recursive sraircase problem
def num_ways(n):
    if n==0 or n==1:
        return 1
    else:
        return (num_ways(n-1) + num_ways(n-2))
    
# recursive sraircase problem (multiple steps)
# if we are passing multiple number of steps i.e more than 2 steps of various digits/steps

def num_ways2(n):
    total = 0
    if n == 0:
        return 1
    for i in {1,3,5}:
        if n-i >= 0:
            total += num_ways2(n-i)
    return total



print("Enter a number to calculate its factorial")
num = int(input())
fact_result = fact(num)
print(fact_result)

num1 = fib(num)
print(num1)

num2=num_ways(num)
print("2 steps",num2)


# x = {1,2,3}
num3 = num_ways2(num)
print("multiple steps",num3)
