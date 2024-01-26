def my_function():
    print("Hello from a function")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Funtion!, I wish you %s"%(username, greeting))

def sum_two_numbers(a,b):
    return a + b


my_function()
my_function_with_args("John Doe", "a great year!")
x = sum_two_numbers(1,2)
print(x)