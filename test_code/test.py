# อย่าพึ่งลบ มาอ่านซ้ำก่อน
"""
    สร้าง class Student โดยกำหนดให้
    - มี attribute ชื่อ name, age, และ student_id ที่เก็บข้อมูลทั่วไปของนักเรียน และ grades ที่เก็บคะแนนของนักเรียนในแต่ละวิชา โดยเป็นโครงสร้างข้อมูลประเภท list
    - มี method ชื่อ add_grade(subject, grade) โดย grade เป็น dictionary ที่เก็บคะแนนของนักเรียนในแต่ละวิชา
        { 
            "subject": "Mathematics", "grade": 85 
        }
    - มี method ชื่อ get_average_grade() ที่คืนค่าเฉลี่ยคะแนนของนักเรียน
    - มี method ชื่อ get_grade_report() ที่คืนค่ารายงานผลการเรียนของนักเรียน
"""

class Student:
    
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []

    # Method to add a grade
    def add_grade(self, grade):
        if grade["grade"] >= 0 and grade["subject"] not in [g["subject"] for g in student.grades]:
            self.grades.append(grade)
        else:
            print("Not sucsedd")

    # Method to get the average grade
    def get_average_grade(self):
        grades_only = [g["grade"] for g in student.grades] 
        avg = sum(grades_only) / len(grades_only)
        return f"{self.name}:  average grade : {avg}"

    # Method to get the grade report
    def get_grade_report(self):
        #subject = [g["subject"] for g in student.grades]
        #return subject
         return f"{self.name}: {self.grades}"


student = Student("John", 20, "S123")
student.add_grade(
    {
        "subject": "Math", 
        "grade": 85
    }
)
student.add_grade(
    {
        "subject": "Science",
        "grade": 92
    }
)
student.add_grade(
    {
        "subject":"Math",
        "grade": 10
    }
)
print(student.get_average_grade())  # Should print 88.5
print(student.get_grade_report())   # Should show all grades
