names = ["ali", "faruk", "osama"]
grades = [100, 50, 75]

connect = zip(names, grades)

info = {}

for student in connect:
    info[student[0]] = student[1]

for key, value in info.items():
    print(f"{key}: {value}")