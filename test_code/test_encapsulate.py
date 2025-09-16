class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def set_length(self,length):
        self.__length = length

    def set_width(self,width):
        self.__width = width

    def calculate_area(self):
        return f"area = {self.__length * self.__width}"
    
    def perimeter(self):
        return f"perimeter = {(self.__length * 2) + (self.__width * 2)}"
    
    def check_square(self):
        if self.__length == self.__width:
            return f"it's a square"
        else:
            return f"it's a not square"

x = Rectangle(1,3)
x.set_length(10)
x.set_length(20)
print(x.calculate_area())
print(x.perimeter())
print(x.check_square())