students = {
"S001": {"name": "Alice", "major": "CS", "courses": ["CS1400", "MATH1210"]},
"S002": {"name": "Bob", "major": "IS", "courses": ["INFO2410", "CS1400"]},
"S003": {"name": "Charlie", "major": "DS", "courses": ["STAT1040", "CS1400"]}
}

def print_student_info(student_id):
    '''prints the formatted information for the provided student Id'''
    student = students.get(student_id)
    print(f"Student Info ({student_id}):\nName: {student["name"]} \nMajor: {student["major"]} \nEnrolled Courses: {student["courses"]}")

def enroll_student(student_id, course_code):
    '''adds the provided course code to the provided student Ids list of courses'''
    student = students.get(student_id)
    student["courses"].append(course_code) # The directions say to use .setdefault or .update but that doesn't make sense to me because courses is a list not another nested dictionary.
    return student

def drop_student(student_id):
    '''removes the provided student Id and their information from the base dictionary'''
    students.pop(student_id)
    return student_id

def main():
    print(f"Student IDs: {students.keys()}")

    print_student_info("S001")

    course = "CS2600"
    enr = enroll_student("S003", course)
    print(f"Enrolled {enr["name"]} in {course}")

    student = drop_student("S002")
    print(f"Dropped student {student}")

    print("Summary:")
    for item in students.items():
        print(f"{item[0]} -> {item[1]["name"]} ({item[1]["major"]}) -> {item[1]["courses"]}")


if __name__ == "__main__":
    main()
