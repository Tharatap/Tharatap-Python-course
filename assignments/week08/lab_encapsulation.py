"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    def __init__(self,length,width):
        self.__length = length
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

square = Rectangle(10,20)
print(square.calculate_area())
print(square.perimeter())
print(square.check_square())

        
        