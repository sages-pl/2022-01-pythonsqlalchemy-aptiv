
grades = []

while True:
    grade = input('What grade you received?: ')

    if not grade:
        break

    grade = float(grade)

    if grade in GRADE_SCALE:
        grades.append(grade)

if grades:
    result = sum(grades) / len(grades)
