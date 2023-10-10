# Sum

# Can apply a default value to a arg
def sum_def(x: float, y: float, z: float = 0):
    print(x + y + z)


# Named param
sum_def(y=1, x=2)
