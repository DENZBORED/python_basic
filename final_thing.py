import json

def calculate_grade(score):
    if 80 <= score <= 100:
        return 'A'
    elif 70 <= score < 80:
        return 'B'
    elif 60 <= score < 70:
        return 'C'
    elif 50 <= score < 60:
        return 'D'
    else:
        return 'F'

students = []

with open("student.json", "r", encoding="utf-8") as fhandler:
    data = fhandler.read()


data1 = json.loads(data)

student_count = len(data1)
print(student_count)

for i in range(2):
    print(f"\nEnter data for student {i+1}")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    student_id = input("Student ID: ")
    math = int(input("Math Score (0-100): "))
    science = int(input("Science Score (0-100): "))
    art = int(input("Art Score (0-100): "))
    student_count += 1


    student = {
        "index": student_count,
        "first_name": first_name,
        "last_name": last_name,
        "student_id": student_id,
        "math_score": math,
        "science_score": science,
        "art_score": art,
        "grade_math": calculate_grade(math),
        "grade_science": calculate_grade(science),
        "grade_art": calculate_grade(art)
    }
    
    students.append(student)
alldata = []
alldata.append(data1)
alldata.append(students)


print(students)
with open("student.json", "w", encoding="utf-8") as f:
    json.dump(alldata, f, ensure_ascii=False, indent=2)

