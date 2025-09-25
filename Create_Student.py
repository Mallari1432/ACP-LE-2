class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.id_name = (student_id, student_name)
        self.email = email
        self.grades = grades if grades else {}
        self.courses = courses if courses else set()

    def __str__(self):
        return f"ID: {self.id_name[0]}, Name: {self.id_name[1]}\n" \
               f"Email: {self.email}\n" \
               f"Courses: {', '.join(self.courses) if self.courses else 'None'}\n" \
               f"Grades: {self.grades if self.grades else 'No grades'}"

    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        gpa_scale = {
            'A': 4.0, 'B': 3.0, 'C': 2.0,
            'D': 1.0, 'F': 0.0
        }
        total_points = 0
        for subject, score in self.grades.items():
            if score >= 90:
                grade = 'A'
            elif score >= 80:
                grade = 'B'
            elif score >= 70:
                grade = 'C'
            elif score >= 60:
                grade = 'D'
            else:
                grade = 'F'
            total_points += gpa_scale[grade]
        return round(total_points / len(self.grades), 2)


class StudentRecords:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        new_student = Student(student_id, student_name, email, grades, courses)
        self.students.append(new_student)
        return "Student added!"

    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.id_name[0] == student_id:
                if email:
                    student.email = email
                if grades:
                    student.grades.update(grades)
                if courses:
                    student.courses.update(courses)
                return "Student updated!"
        return "Student not found."

    def delete_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                self.students.remove(student)
                return "Student deleted!"
        return "Student not found."

    def enroll_course(self, student_id, course):
        for student in self.students:
            if student.id_name[0] == student_id:
                student.courses.add(course)
                return "Course added!"
        return "Student not found."

    def search_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                return str(student)
        return "Student not found."

    def search_by_name(self, name):
        results = []
        for student in self.students:
            if name.lower() in student.id_name[1].lower():
                results.append(str(student))
        return results if results else ["No matches found."]


if __name__ == "__main__":
    records = StudentRecords()
    print(records.add_student("23-97866", "Lara Bels", "23-97866@g.batstate-u.edu.ph"))
    print(records.add_student("24-37809", "Gian Mallari", "24-37809@g.batstate-u.edu.ph", grades={"Math": 85, "English": 73}))
    print(records.update_student("23-97866", grades={"Science": 91}))
    print(records.enroll_course("24-37809", "Physics"))
    print(records.enroll_course("24-37809", "Math"))
    print("\n=== Gian's Info ===")
    print(records.search_student("24-37809"))
    student = next((s for s in records.students if s.id_name[0] == "24-37809"), None)
    if student:
        print(f"\nGian's GPA: {student.calculate_gpa()}")
    print(records.delete_student("23-97866"))
    print("\n=== Search Results for 'Ric' ===")
    for s in records.search_by_name("Ric"):
        print(s)
