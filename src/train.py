import pandas as pd
import joblib
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor
)

data = pd.read_csv("data/students.csv")

X = data[
    [
        "study_hours",
        "attendance",
        "previous_score",
        "assignments_completed",
        "sleep_hours"
    ]
]

y = data["final_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

linear_model = LinearRegression()

tree_model = DecisionTreeRegressor(
    random_state=42
)

forest_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

boost_model = GradientBoostingRegressor(
    random_state=42
)

linear_model.fit(X_train, y_train)

tree_model.fit(X_train, y_train)

forest_model.fit(X_train, y_train)

boost_model.fit(X_train, y_train)

#Save the random Forest model
joblib.dump(
    forest_model,
    "models/student_performance_model.pkl"
)


print("All models trained successfully!")
print("Random Forest model saved successfully!")