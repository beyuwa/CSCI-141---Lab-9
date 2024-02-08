# student

class Student:

    def __init__(ego, name, ide):
        ego.name = name
        ego.id = ide
        ego.major = ''
        ego.age = 0
        ego.courses = []
    
    #def set_name(ego, name):
        #ego.name = name

    #def set_id(ego, ide):
        #ego.id = ide

    def add_course(ego, course_name, credit_hours, grade):
        ego.courses += [(course_name, credit_hours, grade)]
    
    def calculate_gpa(ego):
        courses = ego.courses
        topsum = 0
        botsum = 0

        for i in range(len(courses)):
            credit_hours = courses[i][1]
            grade = courses[i][2]
            topsum += (credit_hours * grade)
            botsum += credit_hours

        if botsum == 0:
            botsum += 1

        GPA = (topsum / botsum)
        
        return GPA
    
