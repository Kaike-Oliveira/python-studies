# Lambda function with sum

# Normal function
def execute(func, *args):
    return func(*args)


def sum_values(x, y):
    return x + y


# Lambda function
print(execute(lambda x, y: x + y, 2, 5))  # Lambda
print(sum_values(2, 5))  # Default
