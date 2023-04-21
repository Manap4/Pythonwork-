class Student:
    def __init__(self, name, estates, course):
        self.name = name
        self.course = course
        self.estates = estates

    def main():
        student = get_student()
        print(f"{student.name}is from {student.estates} and is doing {student.course}")


    def get_student():
        name = input("What is your name?").strip()
        estates = input("Which estate do you come from?").strip()
        course = input("Which course do you do?").strip()
        student = Student(name,estates,course)
        return student
    
    if __name__ == "__main__":
        main()

