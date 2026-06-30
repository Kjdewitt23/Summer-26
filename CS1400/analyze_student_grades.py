def get_score(item):
    '''Helper function to get second item in tuple of student name and score.'''
    return item[1]

def analyze_grades(student_data):
    '''Function to get average, max, and min score from a list of tuples.'''
    total = 0
    for x in student_data:
        total += x[1]
    average = total / len(student_data)
    # I'm not sure if there's a cleaner or easier way to do this. What I was finding is that doing max(or min) was comparing the names and not the scores. So I had to add the helper function to get the second item in the tuple to be compared.
    max_score = max(student_data, key=get_score)
    min_score = min(student_data, key=get_score)

    return average, max_score, min_score

def main():
    students = [("Bob", 92), ("Rick", 60), ("Sandy", 99), ("Eugene", 75), ("Ward", 82)]

    average, max, min = analyze_grades(students)

    print(f"Average grade: {average}")
    print(f"Highest grade: {max[1]} ({max[0]})")
    print(f"Lowest grade: {min[1]} ({min[0]})")

if __name__ == "__main__":
    main()
