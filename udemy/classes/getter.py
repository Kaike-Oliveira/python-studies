# Getter

# Python Method

class Pen:
    def __init__(self, color):
        self.color = color

    @property  # works like an attribute
    def get_color(self):
        return self.color


blue_pen = Pen('Blue')
print(blue_pen.color)

# Default method

# class Pen:
#     def __init__(self, color):
#         self.color = color
#
#     def get_color(self):
#         print('Get Color:')
#         return self.color
#
#
# pen = Pen('Blue')
# print(pen.get_color())
