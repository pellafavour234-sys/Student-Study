import numpy as np
import pandas as pd

np.random.seed(42)

number_of_students = 1000

study_hours = np.random.uniform(1, 10, number_of_students)
attendance = np.random.uniform(50, 100, number_of_students)
previous_score = np.random.uniform(40, 95, number_of_students)
assignments_completed = np.random.randint(3, 11, number_of_students)
sleep_hours = np.random.uniform(4, 9, number_of_students)

final_score = (
    0.25 * study_hours * 10
    + 0.25 * attendance
    + 0.35 * previous_score
    + 1.5 * assignments_completed
    + 1.5 * sleep_hours
)

final_score += np.random.normal(0, 5, number_of_students)

final_score = np.clip(final_score, 0, 100)

data = pd.DataFrame({
    "study_hours": study_hours,
    "attendance": attendance,
    "previous_score": previous_score,
    "assignments_completed": assignments_completed,
    "sleep_hours": sleep_hours,
    "final_score": final_score
})

data.to_csv("data/students.csv", index=False)

print("Dataset created successfully!")
print(data.head())