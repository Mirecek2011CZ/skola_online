class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.classroom = None
        self.grades = {}

    def __repr__(self):
        return f"ID: {self.id}, Name: {self.name}, Classroom: {self.classroom}, Grades: {self.grades}"

class Classroom:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"ID: {self.id}, Name: {self.name}"

class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"ID: {self.id}, Name: {self.name}"

def create_student():
    id = input("Zadej ID studenta: ")
    name = input("Zadej jmeno studenta: ")
    return Student(id, name)

def create_classroom():
    id = input("Zadej ID tridy: ")
    name = input("Zadej jmeno tridy: ")
    return Classroom(id, name)

def create_subject():
    id = input("Zadej ID predmetu: ")
    name = input("Zadej jmeno predmetu: ")
    return Subject(id, name)

def assign_student_to_classroom(student, classroom):
    student.classroom = classroom
    print(f"Student {student.name} pridelen do ucebny: {classroom.name}.")

def add_grade_to_student(student, subject, grade):
    student.grades[subject.name] = grade
    print(f"Znamka {grade} pridana {student.name} do predmetu {subject.name}.")

def main():
    students = []
    classrooms = []
    subjects = []

    while True:
        print("\nMHlavni menu:")
        print("1. Vytvoreni/uprava/smazani studenta")
        print("2. Vytvoreni/uprava/smazani tridy")
        print("3. Vytvoreni/uprava/smazani predmetu")
        print("4. Prirazeni studenta do tridy")
        print("5. Pridani znamky studentovi")
        print("0. Ukonceni")

        option = input("Vyber si moznost: ")

        if option == "1":

            student_id = input("Zadej ID studenta: ")
            existing_student = next((s for s in students if s.id == student_id), None)

            if existing_student:
                print(f"Uprava studenta: {existing_student}")
            else:
                student = create_student()
                students.append(student)
                print("Student byl uspesne vytvoren")

        elif option == "2":
            classroom_id = input("Zadej ID tridy: ")
            existing_classroom = next((c for c in classrooms if c.id == classroom_id), None)

            if existing_classroom:
                print(f"Uprava tridy: {existing_classroom}")
            else:
                classroom = create_classroom()
                classrooms.append(classroom)
                print("Trida byla uspesne vutvorena")

        elif option == "3":
            subject_id = input("Zadej ID predmetu: ")
            existing_subject = next((s for s in subjects if s.id == subject_id), None)

            if existing_subject:
                print(f"Uprava predmetu: {existing_subject}")
            else:
                subject = create_subject()
                subjects.append(subject)
                print("Predmet byl uspesne vytvoren.")

        elif option == "4":
            student_id = input("Zdej ID studenta: ")
            classroom_id = input("Zadej ID tridy: ")

            student = next((s for s in students if s.id == student_id), None)
            classroom = next((c for c in classrooms if c.id == classroom_id), None)

            if student and classroom:
                assign_student_to_classroom(student, classroom)
            else:
                print("Student nebo trida nebyli nalezeni.")

        elif option == "5":
            subject_id = input("Zadej ID predmetu: ")
            grade = input("Zadej znamku: ")

            student = next((s for s in students if s.id == student_id), None)
            subject = next((s for s in subjects if s.id == subject_id), None)

            if student and subject:
                add_grade_to_student(student, subject, grade)
            else:
                print("Student nebo predmet nebyl nalezen.")

        elif option == "0":
            print("Ukoncovani")
            break

        else:
            print("Neplatna moznost.")

if __name__ == "__main__":
    main()