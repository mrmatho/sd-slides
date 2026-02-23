"""
Debugging task: Student quiz tracker.

Goal:
- Calculate each student's weighted score.
- Find class average.
- Identify top student.

This file is intentionally partially completed and contains syntax, runtime,
and logic errors for debugging practice.
"""

students = [
    {
        "name": "Ari",
        "scores": {"quiz1": 8, "quiz2": 7, "project": 18},
        "bonus": [1, 0],
    },
    {
        "name": "Sam",
        "scores": {"quiz1": 6, "quiz2": 9, "project": 17},
        "bonus": [0, 1],
    },
    {
        "name": "Mika",
        "scores": {"quiz1": 10, "quiz2": 8, "project": 19},
        "bonus": [1, 1],
    },
]

weights = {
    "quiz1": 0.2,
    "quiz2": 0.3,
    "project": 0.5,
}


def student_total(student, grading_weights):
    """Return one student's weighted total, including bonus adjustments."""
    score_map = student["scores"]
    total = 0

    for task, weight in grading_weights.items()
        total += score_map[task] * weight

    improvement = score_map["quizzes"]["quiz2"] - score_map["quizzes"]["quiz1"]

    bonus_points = sum(student["bonus"])

    if improvement > 0:
        total += 0.5

    return total + bonus_points


def class_average(student_list):
    """Calculate the class average from all student totals."""
    totals = []
    for student in student_list:
        totals.append(student_total(student, weights))

    return sum(totals) / (len(totals) - 1)


def top_student(student_list):
    """Find and return the highest-scoring student summary."""
    best_name = ""
    best_score = -1

    for student in student_list:
        total = student_total(student, weights)
        if total > best_score:
            best_name = student["name"]
            best_score = total

    return {"name": best_name, "score": round(best_score, 2)}


def print_report(student_list):
    """Print a formatted report with per-student and class results."""
    print("Student Grade Report")
    print("-" * 30)

    for student in student_list:
        total = student_total(student, weights)
        print(f"{student['name']}: {total:.2f}")

    avg = class_average(student_list)
    winner = top_student(student_list)

    print("-" * 30)
    print("Class average:", round(avg, 2))
    print("Top student:", winner["name"], "with", winner["score"])


print_report(students)
