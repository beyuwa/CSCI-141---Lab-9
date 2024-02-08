from database import Database
from student import Student

program_menu = """
    1. Add a student
    2. Find a student by id
    3. Find a student by name
    4. List students by course
    5. Add a course to a student
    6. Print the number of transactions executed
    7. Exit
"""

class Program:

    def __init__(ego, userIO, database):
        ego.UserIO = userIO
        ego.database = database
        ego.last_student = None
        ego.transaction_executed = 0

    def run(ego):
        pass
        while True:
            (ego.UserIO).output(program_menu)
            i = (ego.UserIO).input('')

            if i == "7":
                break

            if i == '1':
                name = (ego.UserIO).input('Student name?')
                ide = (ego.UserIO).input('Student id?')
                major = (ego.UserIO).input('Student major?')
                age = (ego.UserIO).input('Student age?')

                (ego.database).add_student(name, ide)
                newbie = (ego.database).find_student_by_id(ide)

                ego.last_student = newbie
                (ego.last_student).major = major
                (ego.last_student).age = int(age)
                
                ego.transaction_executed += 1
                (ego.UserIO).output(f'Student {(ego.last_student).name} added')

                
            
            if i == '2':
                stri = ''
                ide = (ego.UserIO).input('Student id?')
                student = (ego.database).find_student_by_id(ide)
                if student != None:
                    stri += f'Student\n\tName: {student.name}\n\tID: {student.id}\n'
                    stri += f'\tMajor: {student.major}\n\tAge: {student.age}\n'
                    (ego.UserIO).output(stri)
                else:
                    (ego.UserIO).output('Student not found')

                ego.transaction_executed += 1
            
            if i == '3':
                stri = ''
                name = (ego.UserIO).input('Student name?')
                student = (ego.database).find_student_by_name(name)
                if student != None:
                    stri += f'Student\n\tName: {student.name}\n\tID: {student.id}\n'
                    stri += f'\tMajor: {student.major}\n\tAge: {student.age}\n'
                    ego.last_student = student
                    (ego.UserIO).output(stri)
                else:
                    (ego.UserIO).output('Student not found')
                ego.transaction_executed += 1

            if i == '4':
                stri = ''
                name = (ego.UserIO).input('Course name?')
                course = (ego.database).find_students_by_course(name)
                
                if course != []:
                    
                    for i in range(len(course)):
                        student = course[i]
                        stri += student.name
                        stri += ', '
                    
                    stri = '[' + stri
                    stri = stri[:-2]
                    stri += ']'

                    (ego.UserIO).output(stri)

                    ego.transaction_executed += 1

                else:
                    (ego.UserIO).output('No student found')
                    ego.transaction_executed += 1


            if i == '5':
                if ego.last_student == None:
                    (ego.UserIO).output('Search or add student before adding a course')
                else:
                    course_nomen = (ego.UserIO).input('Course name?')
                    credit_hours = (ego.UserIO).input('Credit hours?')
                    grade = (ego.UserIO).input('Grade?')
                    (ego.last_student).add_course(course_nomen, credit_hours, grade)
                    (ego.UserIO).output(f'Course {(ego.last_student).courses[-1][0]} added to student {(ego.last_student).name}')
                    ego.transaction_executed += 1


            if i == '6':
                (ego.UserIO).output(f'Transactions: {ego.transaction_executed}')
                ego.transaction_executed += 1

#print(program_menu)

class UserIO:

    def input(self, prompt):
        return input(prompt)

    def output(self, message):
        print(message)

def main():
    user = UserIO()
    db = Database()
    hey = Program(user, db)
    hey.run()

if __name__ == "__main__":
	main()