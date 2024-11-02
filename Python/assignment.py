subjects = {}
total = 0
try:
    noOfSubjects = int(input("Enter the number of subjects: "))
except ValueError:
    print("Please enter an integer")
    exit()

for i in range(noOfSubjects + 1):
    name = input(f"Enter the name of the subject {i}: ")
    marks = int(input(f"Enter the marks of the subject {i}: "))
    subjects[name] = marks
    total += marks

everage = total / len(subjects)
subjects["Total"] = total
subjects["Everage"] = int(everage)

print(subjects)
