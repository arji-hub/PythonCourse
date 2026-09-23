"""
ACTIVITY 2 - FUNCTIONS AND COLLECTIONS
Three exercises with increasing difficulty
Topics: Lists, Tuples, Dictionaries, Sets
"""

# ==========================================
# ACTIVITY 1 - BEGINNER LEVEL
# ==========================================

def beginner_activity():

    def create_student_record(name, student_id, grades_list):
        return {
            "student_info": (name, student_id),
            "grades": grades_list
        }

    def calculate_average(grades_list):
        return round(sum(grades_list) / len(grades_list), 2)

    def get_unique_grades(grades_list):
        return set(grades_list)

    def filter_passing_grades(grades_list, passing_score=75):
        return sorted(
            [grade for grade in grades_list if grade >= passing_score],
            reverse=True
        )

    # Test your functions here
    print("=== BEGINNER ACTIVITY ===")
    student = create_student_record("Maria", 101, [90, 85, 88])
    print(f"Student Record: {student}")

    avg = calculate_average(student['grades'])
    print(f"Average Grade: {avg}")

    unique = get_unique_grades([90, 85, 90, 88, 85])
    print(f"Unique Grades: {unique}")

    passing = filter_passing_grades([90, 65, 88, 72, 95])
    print(f"Passing Grades: {passing}")


# ==========================================
# ACTIVITY 2 - INTERMEDIATE LEVEL
# ==========================================

def intermediate_activity():

    def create_library_inventory():
        return {
            "1984": ("George Orwell", "Dystopian", 3),
            "To Kill a Mockingbird": ("Harper Lee", "Fiction", 2),
            "The Great Gatsby": ("F. Scott Fitzgerald", "Classic", 1),
            "Brave New World": ("Aldous Huxley", "Dystopian", 0),
            "The Hobbit": ("J.R.R. Tolkien", "Fantasy", 4),
            "Dune": ("Frank Herbert", "Science Fiction", 2)
        }

    def get_books_by_genre(inventory_dict, target_genre):
        return [
            (title, details[0])
            for title, details in inventory_dict.items()
            if details[1] == target_genre
        ]

    def get_all_genres(inventory_dict):
        return {
            details[1]
            for details in inventory_dict.values()
        }

    def get_low_stock_books(inventory_dict, min_quantity=2):
        return {
            title: details
            for title, details in inventory_dict.items()
            if details[2] < min_quantity
        }

    def update_inventory(inventory_dict, book_title, new_quantity):
        if book_title in inventory_dict:
            author, genre, quantity = inventory_dict[book_title]
            inventory_dict[book_title] = (author, genre, new_quantity)

        return inventory_dict

    def get_author_list(inventory_dict):
        return {
            details[0]
            for details in inventory_dict.values()
        }

    # Test your functions here
    print("\n=== INTERMEDIATE ACTIVITY ===")
    library = create_library_inventory()
    print(f"Library Inventory: {library}\n")

    fiction_books = get_books_by_genre(library, "Fiction")
    print(f"Fiction Books: {fiction_books}")

    all_genres = get_all_genres(library)
    print(f"All Genres: {all_genres}")

    low_stock = get_low_stock_books(library, min_quantity=2)
    print(f"Low Stock Books: {low_stock}")

    authors = get_author_list(library)
    print(f"All Authors: {authors}")


# ==========================================
# ACTIVITY 3 - ADVANCED LEVEL
# ==========================================

def advanced_activity():

    def create_student_enrollment_system():
        return {
            "students": {
                "S001": {
                    "name": "John",
                    "courses": ["CS101", "CS102"],
                    "grades": {
                        "CS101": 90,
                        "CS102": 85
                    }
                },
                "S002": {
                    "name": "Jane",
                    "courses": ["CS101", "CS102", "CS103"],
                    "grades": {
                        "CS101": 92,
                        "CS102": 88,
                        "CS103": 95
                    }
                },
                "S003": {
                    "name": "Mark",
                    "courses": ["CS101", "CS103"],
                    "grades": {
                        "CS101": 78,
                        "CS103": 82
                    }
                },
                "S004": {
                    "name": "Anna",
                    "courses": ["CS102", "CS103"],
                    "grades": {
                        "CS102": 91,
                        "CS103": 89
                    }
                }
            },

            "courses": {
                "CS101": (
                    "Intro to Python",
                    ["Programming"],
                    30
                ),
                "CS102": (
                    "Data Structures",
                    ["CS101"],
                    25
                ),
                "CS103": (
                    "Database Systems",
                    ["CS101"],
                    25
                )
            }
        }

    def get_students_in_course(system_dict, course_code):
        return {
            student_id
            for student_id, student in system_dict["students"].items()
            if course_code in student["courses"]
        }

    def find_student_overlap(system_dict, student_id1, student_id2):
        courses1 = set(
            system_dict["students"][student_id1]["courses"]
        )

        courses2 = set(
            system_dict["students"][student_id2]["courses"]
        )

        return courses1 & courses2

    def get_student_gpa(system_dict, student_id):
        grades = system_dict["students"][student_id]["grades"]

        total_points = 0

        for grade in grades.values():
            if grade >= 90:
                points = 4.0
            elif grade >= 80:
                points = 3.0
            elif grade >= 70:
                points = 2.0
            elif grade >= 60:
                points = 1.0
            else:
                points = 0.0

            total_points += points

        return round(total_points / len(grades), 2)

    def get_course_prerequisites(system_dict, course_code):
        return system_dict["courses"][course_code][1]

    def get_students_for_course(system_dict, course_code):
        students = []

        for student_id, student in system_dict["students"].items():
            if course_code in student["courses"]:
                name = student["name"]
                grade = student["grades"].get(course_code)
                students.append((name, grade))

        return students

    def get_courses_by_average_grade(system_dict):
        course_averages = []

        for course_code in system_dict["courses"]:
            grades = []

            for student in system_dict["students"].values():
                if course_code in student["courses"]:
                    grades.append(student["grades"][course_code])

            if grades:
                average = round(sum(grades) / len(grades), 2)
                course_averages.append((course_code, average))

        return sorted(
            course_averages,
            key=lambda item: item[1],
            reverse=True
        )

    def find_high_performers(system_dict, min_gpa=3.5):
        high_performers = {}

        for student_id in system_dict["students"]:
            gpa = get_student_gpa(system_dict, student_id)

            if gpa >= min_gpa:
                high_performers[student_id] = gpa

        return high_performers

    # Test your functions here
    print("\n=== ADVANCED ACTIVITY ===")
    system = create_student_enrollment_system()
    print("System created!")

    students_in_cs101 = get_students_in_course(system, "CS101")
    print(f"Students in CS101: {students_in_cs101}")

    overlap = find_student_overlap(system, "S001", "S002")
    print(f"Common courses for S001 & S002: {overlap}")

    gpa = get_student_gpa(system, "S001")
    print(f"Student S001 GPA: {gpa}")

    prereqs = get_course_prerequisites(system, "CS102")
    print(f"Prerequisites for CS102: {prereqs}")

    course_avg = get_courses_by_average_grade(system)
    print(f"Courses by avg grade: {course_avg}")

    high_performers = find_high_performers(system, min_gpa=3.5)
    print(f"High performers (GPA >= 3.5): {high_performers}")


# ==========================================
# RUN ALL ACTIVITIES
# ==========================================

if __name__ == "__main__":
    beginner_activity()
    intermediate_activity()
    advanced_activity()