class Course:
    def __init__(self, name, teacher, students):
        self.name = name
        self.teacher = teacher
        self.students = students

    def average_score(self):
        if not self.students:
            return 0

        return sum(self.students.values()) / len(self.students)


class School:
    def __init__(self):
        self.courses = []

    def add_course(self, name, teacher, students):
        self.courses.append(Course(name, teacher, students))

    def print_report(self):
        print("School Report")
        print("=============")

        for course in self.courses:
            print(f"Course: {course.name}")
            print(f"Teacher: {course.teacher}")
            print(f"Average Score: {course.average_score():.2f}")

            for student, score in course.students.items():
                print(f"  {student}: {score}")

            print("-------------")


school = School()

school.add_course(
    "Mathematics",
    "Mr. Carter",
    {
        "Alice": 92,
        "Brian": 85,
        "Clara": 97
    }
)

school.add_course(
    "Physics",
    "Ms. Stone",
    {
        "David": 88,
        "Emma": 91,
        "Frank": 84
    }
)

school.add_course(
    "Computer Science",
    "Mr. Brooks",
    {
        "Grace": 96,
        "Henry": 89,
        "Ivy": 94
    }
)

school.print_report()
