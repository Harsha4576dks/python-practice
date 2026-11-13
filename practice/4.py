def students ():
    students = {
        "Harsha": 85,
        "Rahul": 92,
        "Kiran": 78,
        "Arun": 95
    }

    highest_marks = 0
    top_student = ""

    for name, marks in students.items():
       if marks > highest_marks:
           highest_marks = marks
           top_student = name

    print(top_student)
    print(highest_marks)

students()