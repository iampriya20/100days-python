# day43_grade_calculator.py

print("📊 Grade Calculator")

marks = []
subjects = int(input("Enter number of subjects: "))

for i in range(subjects):
    score = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(score)

total = sum(marks)
average = total / subjects

# Simple grading logic
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"\n📝 Total Marks: {total}")
print(f"📉 Average: {average:.2f}")
print(f"🎓 Grade: {grade}")
