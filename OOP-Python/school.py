"""
- PROJECT - Basic Student, Teacher and Course creation, w/ menu
"""


class Course:
    def __init__(self, courseName):
        self.courseName = courseName

    @staticmethod
    def getInfo(teachList):
        print("\n-- COURSES --")
        for course in teachList:
            print(course.courseName)


class Teacher:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

    @staticmethod
    def getInfo(teachList):
        print("\n-- TEACHERS --")
        for teacher in teachList:
            print(teacher.name, teacher.lastName)


class Student:
    def __init__(self, name, lastName, age):
        self.name = name
        self.lastName = lastName
        self.age = age

    @staticmethod
    def getInfo(studList):
        print("\n-- STUDENTS --")
        for stud in studList:
            print(stud.name, stud.lastName)


# MAIN

listStudents = list()
listTeacher = list()
listCourses = list()
dictGroup = {}

while True:
    print("|| WELCOME TO THE SCHOOL ||")
    print("1. Create User\n2. Create Course\n3. Assign Users to Courses\n4. Print All\n5. Exit")
    option = int(input("Enter your option: "))

    if option == 1:
        name = str(input("Enter your NAME: "))
        lastName = str(input("Enter your LAST NAME: "))
        role = int(input("Write your ROLE (student[0] or teacher[1]): "))

        if role == 0:
            age = int(input("Enter your AGE: "))
            listStudents.append(Student(name, lastName, age))
        elif role == 1:
            listTeacher.append(Teacher(name, lastName))

    elif option == 2:
        courseName = str(input("Enter the NAME of the COURSE: "))

        Student.getInfo(listStudents)
        Teacher.getInfo(listTeacher)

        listCourses.append(Course(courseName))

        Course.getInfo(listCourses)
        print("\n")
    elif option == 3:
        if len(listStudents) == 0 or len(listTeacher) == 0 or len(listCourses) == 0:
            print("!! NOT ENOUGH PERSONNEL TO ASSIGN !!\n")
        else:

            Student.getInfo(listStudents)
            Teacher.getInfo(listTeacher)
            Course.getInfo(listCourses)

            print("\n")

            courseInsert = int(
                input(f"What course you want to insert personnel into? ((choose from 0 - {len(listCourses) - 1})"))
            studentInsert = int(
                input(
                    f"What Student do you want in the course {listCourses[courseInsert].courseName} (choose from 0 - {len(listStudents) - 1})"))  # NOQA: E501
            teacherInsert = int(
                input(
                    f"What Teacher do you want in the course {listCourses[courseInsert].courseName} (choose from 0 - {len(listTeacher) - 1})"))  # NOQA: E501

            if listCourses[courseInsert].courseName in dictGroup:
                dictGroup[listCourses[courseInsert].courseName].extend([listStudents[studentInsert].name])
            else:
                dictGroup[listCourses[courseInsert].courseName] = []
                dictGroup[listCourses[courseInsert].courseName].extend([listStudents[studentInsert].name])
            print(dictGroup)
    elif option == 4:
        Student.getInfo(listStudents)
        Teacher.getInfo(listTeacher)
        Course.getInfo(listCourses)
        print("\n-- GROUPS --\n", dictGroup)
    elif option == 5:
        break
    else:
        print("!! NOT A VALID VALUE !!\n")
