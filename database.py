from student import Student

class Database:

    def __init__(ego):
        ego.__students = []

    def add_student(ego, name, ide):
        newStew = Student(name, ide)
        ego.__students += [newStew]

        return newStew

    def find_student_by_id(ego, ide):
        for i in range(len(ego.__students)):
            if ego.__students[i].id == ide:
                return ego.__students[i]
        
        return None

    def find_student_by_name(ego, name):
        for i in range(len(ego.__students)):
            if ego.__students[i].name == name:
                return ego.__students[i]
    
        return None

    def find_students_by_course(ego, course_nomen):
        database = []
        for i in range(len(ego.__students)):
            for j in range(len((ego.__students[i]).courses)):
                print(((ego.__students[i]).courses)[j][0])
                if ((ego.__students[i]).courses)[j][0] == course_nomen:
                    database += [ego.__students[i]]
                    j = len((ego.__students[i]).courses)
        
        ego.__database = database
        
        return database

    def num_student(ego):
        database = ego.__students
        return(len(database))