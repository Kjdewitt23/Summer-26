from dataclasses import dataclass, field

@dataclass(order=True)
class Student:
    id: int
    name: str
    major: str
    courses: list[str] = field(default_factory=list)

    def enroll(self, course: str):
        self.courses.append(course)

    def total_courses(self):
        return len(self.courses)

def enroll_in_courses(student: Student, courses: list[str]):
    for course in courses:
        student.enroll(course)

def main():
    bob = Student(1, "Bob", "CS")
    rick = Student(2, "Rick", "Botany")
    sandy = Student(3, "Sandy", "Micro-biology")

    bob_courses = ["CS 2550", "CS 4800", "CS 3250"]
    rick_courses = ["BOT 1050", "BOT 1090"]
    sandy_courses = ["BIO 4560", "BIO 5550", "BIO 6500"]

    enroll_in_courses(bob, bob_courses)
    enroll_in_courses(rick, rick_courses)
    enroll_in_courses(sandy, sandy_courses)

    print(bob)
    print(rick)
    print(sandy)

    print(bob.total_courses())
    print(rick.total_courses())
    print(sandy.total_courses())

    print(bob < rick)
    print(sandy > bob)

if __name__ == "__main__":
    main()

# REFLECTION QUESTIONS:

#1: We use default_factory because if we didn't then the list would be attached to every instance of the class so it would be a shared list and not a new one for each instance.

#2: It would be nearly impossible to know what data belonged to which student.

#3: It helps keep the code concise. They're shared functions that each instance needs access to and making them methods allows for shorter calls such as lines 37 - 39.
# They also allow functions like enroll_in_courses() to be simpler by calling student.enroll instead of writing an entirely new helper or inner function. 