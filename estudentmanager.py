students = {}


def menu():
    width = 40
    print("="*width)

    title = "student grade manager"
    print( title.upper().center(width))

    print("="*width)
    print(" ")

    print("1. Add student")
    print("2. Add Grade")
    print("3. View Student")
    print("4. Show All Students")
    print("5. Show Student Average")
    print("6. Show Class Average")
    print("7. Exit")

    print()
    choice = input("Choose an option: ")
    return choice 

def add_student():
    name = input("Enter student name: ")
    name = name.strip().title()

    if not name: #it can be write if name == "":
        print("Student name can not be empty.")
        return

    if name in students:
        print("Student already exists.")
        return
 
    students[name] = []
    print("Student added successfully.")
    return


def add_grade():
    name = input("Enter student name: ")
    name = name.strip().title()

    if name not in students:
        print("Student not found.")
        return

    grade = int(float(input("Enter student grade: ")))

    if 0 <= grade <= 20:
        students[name].append(grade)
        print("Grade added successfully")

    else:
        print("Grade must be between 0 and 20.")
        return

def view_student():
    name = input("Enter student name: ")
    name = name.strip().title()

    if name not in students:
        print("Student not found")
        return

    print("\nStudent:", name, "\n") 
      
    if not students[name]:
        print("Grades: No grades available")

    print("Grades:", students[name])
 
    
def show_all_students():
    if not students:
        print("No students registered.")
        return

    for name in students:
        print(name)

        if not students[name]:
            print("Grades: No grades available")

        else:
            print("Grades:", students[name])

def show_student_average():
    name = input("Enter student name: ")
    name = name.strip().title()

    if name not in students:
        print("Students not found")
        return

    if not students[name]:
        print("Grades: No grades available")

    else:
        average = sum(students[name])/len(students[name])
        print(f"Average: {average:.2f}")

def show_class_average():
    if not students:
        print("No students registered")
        return

    total = 0
    number_of_grades = 0

    for name in students:
        total += sum(students[name])
        number_of_grades += len(students[name])

    if number_of_grades == 0 :
        print("No grades available.")
        return
    
    class_average = total / number_of_grades
    print(f"Class Average: {class_average:.2f}")
        
def main():
    while True: 
        choice = menu()

        if choice == "1":
            add_student()

        elif choice == "2":
            add_grade()

        elif choice == "3":
            view_student()

        elif choice == "4":
            show_all_students()

        elif choice == "5":
            show_student_average()

        elif choice == "6":
            show_class_average()

        elif choice == "7":
            print("\nThank you for using Student Manager.")
            print("Goodbye!\n")
            break

        else:
            print("\ninvalid option. Please choose a number between 1 and 7.\n")



main()