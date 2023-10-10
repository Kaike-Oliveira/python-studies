# Sum

# Can apply a default value to a arg
def sum_def(x: float, y: float, z: float = 0):
    # Define a variable inside a function scope
    sum_result = x + y + z

    # Can return a result to a function
    return sum_result


# Named param
sum_def(y=1, x=2)
print(sum_def(y=1, x=2))
