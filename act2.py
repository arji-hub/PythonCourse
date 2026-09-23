"""
ACTIVITY 2 - FUNCTIONS AND COLLECTIONS
Three exercises with increasing difficulty
Topics: Lists, Tuples, Dictionaries, Sets
"""

# ==========================================
# ACTIVITY 1 - BEGINNER LEVEL
# ==========================================
"""
BEGINNER ACTIVITY: Student Grade Management System

Create a program that manages student grades using basic collections.
You will work with:
- Lists (store grades)
- Tuples (store immutable student info)
- Dictionaries (map students to grades)
- Sets (find unique grades)
"""


def beginner_activity():
    """
    TODO: Complete the following functions
    """

    def create_student_record(name, student_id, grades_list):
        """
        Create a student record combining different data types.

        Args:
            name (str): Student name
            student_id (int): Student ID
            grades_list (list): List of grades [90, 85, 88]

        Returns:
            dict: Student record with student info (tuple) and grades (list)

        Example:
            create_student_record("Juan", 101, [90, 85, 88])
            # Should return:
            # {'student_info': ('Juan', 101), 'grades': [90, 85, 88]}
        """
        pass

    def calculate_average(grades_list):
        """
        Calculate the average of a list of grades.

        Args:
            grades_list (list): List of numeric grades

        Returns:
            float: Average grade rounded to 2 decimal places

        Example:
            calculate_average([90, 85, 88])  # Returns: 87.67
        """
        pass

    def get_unique_grades(grades_list):
        """
        Get unique grades from a list using a set.

        Args:
            grades_list (list): List of grades (may contain duplicates)

        Returns:
            set: Set of unique grades

        Example:
            get_unique_grades([90, 85, 90, 88, 85])  # Returns: {85, 88, 90}
        """
        pass

    def filter_passing_grades(grades_list, passing_score=75):
        """
        Filter grades that meet or exceed the passing score.

        Args:
            grades_list (list): List of grades
            passing_score (int): Minimum passing score (default: 75)

        Returns:
            list: List of passing grades in descending order

        Example:
            filter_passing_grades([90, 65, 88, 72, 95])  # Returns: [95, 90, 88]
        """
        pass

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
"""
INTERMEDIATE ACTIVITY: Library Inventory Management

Create a system to manage a library's book inventory.
You will work with:
- Lists (store book details)
- Tuples (immutable book info)
- Dictionaries (map books to inventory counts and details)
- Sets (track genres, authors)
"""


def intermediate_activity():
    """
    TODO: Complete the following functions
    """

    def create_library_inventory():
        """
        Create a sample library inventory.

        Returns:
            dict: Dictionary with book titles as keys and
                  tuple (author, genre, quantity) as values

        Example return structure:
            {
                "1984": ("George Orwell", "Dystopian", 3),
                "To Kill a Mockingbird": ("Harper Lee", "Fiction", 2)
            }
        """
        pass

    def get_books_by_genre(inventory_dict, target_genre):
        """
        Get all books of a specific genre.

        Args:
            inventory_dict (dict): Library inventory
            target_genre (str): Target genre to filter

        Returns:
            list: List of tuples (book_title, author) for books in that genre

        Example:
            get_books_by_genre(inventory, "Fiction")
            # Returns: [("1984", "George Orwell"), ...]
        """
        pass

    def get_all_genres(inventory_dict):
        """
        Get all unique genres in the library.

        Args:
            inventory_dict (dict): Library inventory

        Returns:
            set: Set of all unique genres

        Example:
            get_all_genres(inventory)
            # Returns: {"Dystopian", "Fiction", "Science Fiction"}
        """
        pass

    def get_low_stock_books(inventory_dict, min_quantity=2):
        """
        Find books with low stock (below minimum quantity).

        Args:
            inventory_dict (dict): Library inventory
            min_quantity (int): Minimum acceptable quantity (default: 2)

        Returns:
            dict: Dictionary of low stock books with their details

        Example:
            {
                "The Great Gatsby": ("F. Scott Fitzgerald", "Classic", 1),
                "Brave New World": ("Aldous Huxley", "Dystopian", 0)
            }
        """
        pass

    def update_inventory(inventory_dict, book_title, new_quantity):
        """
        Update the quantity of a specific book.

        Args:
            inventory_dict (dict): Library inventory
            book_title (str): Title of the book
            new_quantity (int): New quantity to set

        Returns:
            dict: Updated inventory dictionary
        """
        pass

    def get_author_list(inventory_dict):
        """
        Get all unique authors in the library.

        Args:
            inventory_dict (dict): Library inventory

        Returns:
            set: Set of all unique authors
        """
        pass

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
"""
ADVANCED ACTIVITY: Student Course Enrollment & Analytics

Create a comprehensive system for managing student course enrollments with analytics.
You will work with:
- Lists (store course lists, enrollment records)
- Tuples (immutable course info, grades)
- Dictionaries (complex nested structures for courses, students, grades)
- Sets (find common courses, unique prerequisites)
"""


def advanced_activity():
    """
    TODO: Complete the following functions
    """

    def create_student_enrollment_system():
        """
        Create a complex student enrollment system.

        Returns:
            dict: Nested dictionary structure:
            {
                "students": {
                    "S001": {
                        "name": "John",
                        "courses": ["CS101", "CS102"],
                        "grades": {"CS101": 90, "CS102": 85}
                    }
                },
                "courses": {
                    "CS101": ("Intro to Python", ["Programming"], 30),
                    "CS102": ("Data Structures", ["Programming", "CS101"], 25)
                }
            }

            Note: Course value is tuple: (course_name, prerequisites, capacity)
        """
        pass

    def get_students_in_course(system_dict, course_code):
        """
        Get all students enrolled in a specific course.

        Args:
            system_dict (dict): The enrollment system
            course_code (str): Course code (e.g., "CS101")

        Returns:
            set: Set of student IDs enrolled in the course

        Example:
            get_students_in_course(system, "CS101")
            # Returns: {"S001", "S002", "S003"}
        """
        pass

    def find_student_overlap(system_dict, student_id1, student_id2):
        """
        Find courses that two students have in common.

        Args:
            system_dict (dict): The enrollment system
            student_id1 (str): First student ID
            student_id2 (str): Second student ID

        Returns:
            set: Set of common course codes

        Example:
            find_student_overlap(system, "S001", "S002")
            # Returns: {"CS101", "CS102"}
        """
        pass

    def get_student_gpa(system_dict, student_id):
        """
        Calculate GPA for a student (assuming 4.0 scale mapping: 90+=4.0, 80+=3.0, etc).

        Args:
            system_dict (dict): The enrollment system
            student_id (str): Student ID

        Returns:
            float: Student GPA rounded to 2 decimal places
        """
        pass

    def get_course_prerequisites(system_dict, course_code):
        """
        Get all prerequisites for a course.

        Args:
            system_dict (dict): The enrollment system
            course_code (str): Course code

        Returns:
            list: List of prerequisite course codes

        Example:
            get_course_prerequisites(system, "CS102")
            # Returns: ["CS101"]
        """
        pass

    def get_students_for_course(system_dict, course_code):
        """
        Get detailed info about students in a course (name, grade).

        Args:
            system_dict (dict): The enrollment system
            course_code (str): Course code

        Returns:
            list: List of tuples (student_name, grade)

        Example:
            get_students_for_course(system, "CS101")
            # Returns: [("John", 90), ("Jane", 92)]
        """
        pass

    def get_courses_by_average_grade(system_dict):
        """
        Get all courses sorted by average grade (highest first).

        Args:
            system_dict (dict): The enrollment system

        Returns:
            list: List of tuples (course_code, average_grade)

        Example:
            [("CS102", 88.5), ("CS101", 86.0)]
        """
        pass

    def find_high_performers(system_dict, min_gpa=3.5):
        """
        Find students with GPA above a threshold.

        Args:
            system_dict (dict): The enrollment system
            min_gpa (float): Minimum GPA threshold

        Returns:
            dict: Dictionary of {student_id: gpa} for qualifying students
        """
        pass

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