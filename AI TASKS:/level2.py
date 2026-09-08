study_hours = int(input("Enter the number of hours you study per day: "))
attendance = int(input("Enter your attendance percentage: "))

# convert attendance percentage into a decimal unit
attendance = attendance / 100
study_hours = study_hours /10

weighted_sum = (study_hours * 3.5) + (attendance * 2.0) + (-3.0)

if weighted_sum >= 0:
    print("student would pass the exam easily")
else:
    print("student would fail the exam")
