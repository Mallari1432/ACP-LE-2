class StudentRecords:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        if any(s.id_name[0] == student_id for s in self.students):
            return "Student ID already exists"
        student = Student(student_id, student_name, email, grades, courses)
        self.students.append(student)
        return "Student added successfully"

    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.id_name[0] == student_id:
                if email is not None:
                    student.email = email
                if grades is not None:
                    student.grades = grades
                if courses is not None:
                    student.courses = set(courses)
                return "Student updated successfully"
        return "Student not found"

    
