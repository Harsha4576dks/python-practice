def Rank():

    students = {
    "Rahul": 85,
    "Arun": 95,
    "Kiran": 78,
    "Ravi": 90
}

    highest_rank = ""
    highest_marks = 0

    for name, marks in students.items():
        if marks > highest_marks:
            highest_marks = marks
            highest_rank = name

    print(highest_rank)
    print(highest_marks)

Rank()