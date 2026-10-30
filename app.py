"""
Module: PROG211 - Object-Oriented Programming 1
Assignment: Real-World Solutions under DPG Standards
Domain: Education (Digital Student Learning Portal System)
"""

class Student:
    # Class attribute shared across all students (Task 3: Class & Instance Methods)
    institution_name = "Limkokwing University Digital Portal"
    total_students = 0

    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major
        Student.total_students += 1

    def display_info(self):
        """Task 1 & 3: Instance method to display student details"""
        print(f"ID: {self.student_id} | Name: {self.name} | Major: {self.major}")

    def update_major(self, new_major):
        """Task 1: Instance method to update student record"""
        self.major = new_major
        print(f"[Update] {self.name}'s major changed to {self.major}.")

    @classmethod
    def get_institution_summary(cls):
        """Task 3: Class method operating on class-level attributes"""
        return f"Portal: {cls.institution_name} | Total Registered Students: {cls.total_students}"


class Course:
    def __init__(self, course_code, course_title, credits_and_semester):
        self.course_code = course_code
        self.course_title = course_title
        # Task 2 Bonus: Using a Tuple for fixed course metadata (credits, semester) -> Extra 10 marks eligible!
        self.credits_and_semester = credits_and_semester 

    def display_course_info(self):
        credits, semester = self.credits_and_semester
        print(f"Course: {self.course_code} - {self.course_title} ({credits} Credits, Semester {semester})")


class LearningPortal:
    def __init__(self):
        # Task 2: Using a Dictionary to store multiple objects using unique ID as the key
        self.student_registry = {}

    def add_student(self, student):
        """Task 2: Function to add records to the dictionary data structure"""
        if student.student_id in self.student_registry:
            print(f"Error: Student ID {student.student_id} already exists.")
        else:
            self.student_registry[student.student_id] = student
            print(f"Success: Added {student.name} to the portal registry.")

    def display_all_records(self):
        """Task 2: Function to display records from the dictionary structure"""
        print("\n--- Current Student Learning Portal Registry ---")
        if not self.student_registry:
            print("No records found.")
        else:
            for s_id, student_obj in self.student_registry.items():
                print(f"Key [{s_id}] -> ", end="")
                student_obj.display_info()
        print("------------------------------------------------\n")

    def enroll_interaction(self, student, course):
        """Task 1: Demonstrates interaction between Student and Course objects"""
        print(f"[Interaction] Student {student.name} is successfully enrolled in {course.course_title}!")


# --- Program Execution / Main Block ---
if __name__ == "__main__":
    print("=== STARTING DIGITAL LEARNING PORTAL ===")
    
    # Initialize Portal
    portal = LearningPortal()

    # Create Objects (Task 1)
    s1 = Student("S101", "Aminata Conteh", "Software Engineering")
    s2 = Student("S102", "Mohamed Kamara", "Information Technology")
    
    # Using a tuple for course details (Task 2 Bonus)
    c1 = Course("PROG211", "Object-Oriented Programming 1", (3, 3))

    # Add records using Dictionary structure (Task 2)
    portal.add_student(s1)
    portal.add_student(s2)

    # Display all records stored in the dictionary (Task 2)
    portal.display_all_records()

    # Test Instance and Class Methods (Task 3)
    print("--- Testing Methods ---")
    s1.display_info()                   # Instance Method
    s1.update_major("Cyber Security")   # Instance Method
    print(Student.get_institution_summary()) # Class Method (@classmethod)

    # Test Object Interaction (Task 1)
    print("\n--- Testing Object Interaction ---")
    portal.enroll_interaction(s1, c1)
    c1.display_course_info()
    
    print("\n=== PROGRAM TERMINATED SUCCESSFULLY ===")