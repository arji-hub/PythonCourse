# **Problem:**
# Create a program with functions that:
# - Store student data as a dictionary of dictionaries: `{name: {'math': score, 'english': score, 'science': score}}`
# - Function to add a student with their grades
# - Function to calculate average grade for a student
# - Function to find the student with the highest average
# - Function to display all students and their averages
#
# **Example:**
# ```
# --- Student Grade Manager ---
# 1. Add Student
# 2. View All Students
# 3. Find Top Student
# 4. Exit
#
# Enter choice: 1
# Student name: Alice
# Math grade: 85
# English grade: 90
# Science grade: 88
# Alice added successfully!
#
# Enter choice: 2
# Alice - Average: 87.67
# Bob - Average: 82.33
#
# Enter choice: 3
# Top student: Alice (Average: 87.67)
# ```
#
# **Hints:**
# - Create a global dictionary to store students
# - Write separate functions for each operation
# - Use loops to iterate through dictionaries
# - Format output nicely with f-strings
#
#

students = {}
is_exiting = False

def displayUI():
    print('''--- Student Grade Manager ---
    1. Add Student
    2. View All Students
    3. Find Top Student
    4. Exit
    ''')
    choice = input('Enter Choice :')
    return int(choice)

def addStudent():
    inpName = input('Student name:')
    inpMath = int(input('Math Grade:'))
    inpEnglish = int(input('English Grade:'))
    inpScience = int(input('Science Grade:'))
    student = {
        inpName :{
            'math': inpMath,
            'english': inpEnglish,
            'science': inpScience
        }
    }
    students.update(student)
    print(f'{inpName} added successfully!')

def average(grades):
    return round(sum(grades)/len(grades),2)

def highestAverage():
    highest_name = None
    highest_average = 0

    for name, grades in students.items():
        avg = average(grades.values())
        if avg > highest_average:
            highest_average = avg
            highest_name = name
    print(f'Top student: {highest_name} (Average: {highest_average})')

def displayAll():
    for name, grades in students.items():
        avg = average(grades.values())
        print(f'{name} - Average: {avg}')

def processChoice(choice):
    match choice:
        case 1:
            addStudent()
        case 2:
            displayAll()
        case 3:
            highestAverage()
        case 4:
            return True
    print()
    return False

while not is_exiting:
    choice = displayUI()
    is_exiting = processChoice(choice)