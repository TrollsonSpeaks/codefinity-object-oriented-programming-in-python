class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(4, 5)
print(rect.area())
print(rect.perimeter())