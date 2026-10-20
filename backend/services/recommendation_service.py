def generate_recommendations(data, prediction):

    recommendations = []

    study_hours = data["study_hours"]
    attendance = data["attendance"]
    previous_score = data["previous_score"]
    assignments = data["assignments_completed"]
    sleep = data["sleep_hours"]


    if study_hours < 4:

        recommendations.append({
            "type": "study",
            "title": "Study Pattern",
            "message":
                "The entered study time is relatively low. "
                "Try increasing focused study sessions."
        })


    if attendance < 75:

        recommendations.append({
            "type": "attendance",
            "title": "Attendance",
            "message":
                "Attendance is below 75%. "
                "Improving attendance may support better academic performance."
        })


    if assignments < 5:

        recommendations.append({
            "type": "assignment",
            "title": "Assignments",
            "message":
                "Only a small number of assignments were completed. "
                "Completing more coursework may help."
        })


    if sleep < 6:

        recommendations.append({
            "type": "sleep",
            "title": "Sleep",
            "message":
                "The entered sleep duration is low. "
                "Maintaining a healthy sleep routine can support learning."
        })


    if previous_score < 50:

        recommendations.append({
            "type": "academic",
            "title": "Previous Performance",
            "message":
                "The previous score is relatively low. "
                "Focus on the areas where previous performance was weakest."
        })


    if not recommendations:

        recommendations.append({
            "type": "positive",
            "title": "Strong Profile",
            "message":
                "The entered academic profile does not trigger "
                "any major recommendation rules."
        })


    return recommendations