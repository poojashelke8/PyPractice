# ans = input("enter number")
# print(ans)

# dict1 = dict([(1,5),(2,10),(3,15)])
# dict2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# print(dict1)
# print(dict1[3])
# dict1[4] = 20
# print(dict1)
# del(dict1[2])
# print(dict1)
# print(list(dict1))
x = 5
# try:
#     x//0
# except ZeroDivisionError as err:
#     print("Error......",err)
# else:
#     print("no error")

# try:
#     user_input = input("Enter a number: ")
#     number = int(user_input)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# else:
#     print(f"Entered number: {number}")
# finally:
#     print("Execution completed.")

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    
rev = Reverse('spam')
print(str(iter(rev)))

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
