import numpy as np

#create random marks between 0 and 100 for 30 students
np.random.seed(42)
marks = np.random.randint(0, 101, size=30)

# Show raw marks
print(" Student Marks:", marks)

# Mean
mean_marks = np.mean(marks)
print(f"\n Average (Mean): {mean_marks:.2f}")

# Median
median_marks = np.median(marks)
print(f" Median: {median_marks}")

# Standard Deviation
std_dev = np.std(marks)
print(f" Standard Deviation: {std_dev:.2f}")

# Maximum & Minimum
max_marks = np.max(marks)
min_marks = np.min(marks)
print(f" Highest Mark: {max_marks}")
print(f" Lowest Mark: {min_marks}")

# Pass percentage
pass_count = np.sum(marks >= 35)
pass_percentage = (pass_count / len(marks)) * 100
print(f"Pass Percentage: {pass_percentage:.2f}%")

# Grade distribution
def assign_grade(score):
    if score >= 85:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 50:
        return 'C'
    elif score >= 35:
        return 'D'
    else:
        return 'F'

grades = np.array([assign_grade(m) for m in marks])
unique, counts = np.unique(grades, return_counts=True)
grade_distribution = dict(zip(unique, counts))

print("\n Grade Distribution:")
for grade, count in grade_distribution.items():
    print(f"  Grade {grade}: {count} students")


import matplotlib.pyplot as plt

plt.bar(grade_distribution.keys(), grade_distribution.values(), color='skyblue')
plt.title("Grade Distribution")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.grid(axis='y')
plt.show()
