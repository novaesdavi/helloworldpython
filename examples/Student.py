from Person import Person


class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id

    def get_student_info(self):
        return f"Name: {self.first_name} {self.last_name} , Age: {self.age}, Student ID: {self.student_id}"