class Rectangle:
    default_color = 'green'
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, w):
        if w<=0:
            raise Warning('width must be greater than 0')
        self.__width = w

    @height.setter
    def height(self, h):
        if h<=0:
            raise Warning('height must be greater than 0')
        self.__height = h


rectangle = Rectangle(10, 20)
print(rectangle.area())
print(rectangle.width)
rectangle.width = 20
print(rectangle.area())