"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area
    def get_area(self):
        area = self.length * self.width
        return area

    # Method to get the perimeter
    def get_perimeter(self):
        perimeter = (self.length * 2) + (self.width * 2)
        return perimeter


rect = Rectangle(10, 5)
print(f"area: {rect.get_area()}")       # Should print 50
print(f"perimeter: {rect.get_perimeter()}")  # Should print 30

class Circle:
    def __init__(self,r):
        self.r = r
        print("Circle created!!")
   
    def get_area(self):
        return f"area Circle: {3.14 * (self.r ** 2):.2f}"
    
    def get_perimeter(self):
        return f"perimeter Circle:  {2 * 3.14 * self.r:.2f}"
circle1 = Circle(5)
print(circle1.get_area())
print(circle1.get_perimeter())
    