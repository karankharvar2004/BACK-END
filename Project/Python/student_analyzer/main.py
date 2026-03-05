from student import Student
from database import save_student
from analysis import analyze_data, search_student, find_topper, show_ranking
from visualization import show_graph, subject_graph


def menu():

    print("\n===== Student Performance Analyzer =====")
    print("1. Add Student")
    print("2. Class Statistics")
    print("3. Show Student Graph")
    print("4. Search Student")
    print("5. Find Topper")
    print("6. Show Rankings")
    print("7. Subject Average Graph")
    print("8. Exit")


while True:

    menu()

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter name: ")
        roll = input("Enter roll: ")

        m1 = int(input("Math: "))
        m2 = int(input("Science: "))
        m3 = int(input("English: "))

        marks = [m1, m2, m3]

        s = Student(name, roll, marks)

        save_student(s)

        print("Student saved!")

    elif choice == "2":
        analyze_data()

    elif choice == "3":
        show_graph()

    elif choice == "4":
        search_student()

    elif choice == "5":
        find_topper()

    elif choice == "6":
        show_ranking()

    elif choice == "7":
        subject_graph()

    elif choice == "8":
        break