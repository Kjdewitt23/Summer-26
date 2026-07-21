def calculate_average(grades):
    '''Sums the numbers in a list then divides by the length of that list to find average'''
    if len(grades) == 0:
        return "N/A"
    else:
        return sum(grades) / len(grades)

def process_grades(grades):
    '''Creates a new list of valid grades, uses helper function calculate_average to get the average, then distributes the letter grades based on score using an inner function.'''
    valid_grades = [x for x in grades if 0 <= x <= 100]
    average_grade = calculate_average(valid_grades)
    grade_dis = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

    def grade_distribution():
        '''Updates the values in the grade_dis dictionary based on numeric value'''
        for grade in valid_grades:
            if grade >= 90:
                grade_dis['A'] += 1
            elif grade >= 80:
                grade_dis['B'] += 1
            elif grade >= 70:
                grade_dis['C'] += 1
            elif grade >= 60:
                grade_dis['D'] += 1
            else:
                grade_dis['F'] += 1

        return grade_dis
    
    grade_dis = grade_distribution()  #I was running into a dumb issue where I forgot to call this inner function and it took me a while to figure out that was the issue.
    return valid_grades, average_grade, grade_dis

def main():
    grades = [95, 82, -10, 76, 59, 89, 101]

    valid, average, dis = process_grades(grades)

    print(f"Valid grades: {valid}")
    print(f"Average grade: {average}")
    print(f"Grade distribution: {dis}")

if __name__ == "__main__":
    main()