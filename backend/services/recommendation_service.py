def recommend_resources(

    risk,

    persona,

    confusion_score
):

    recommendations = []

    # =====================================
    # HIGH CONFUSION
    # =====================================

    if confusion_score > 40:

        recommendations.append(
            "Short concept revision videos"
        )

        recommendations.append(
            "Step-by-step practice problems"
        )

    # =====================================
    # PERSONA-BASED
    # =====================================

    if persona == "Silent Isolator":

        recommendations.append(
            "Peer discussion groups"
        )

        recommendations.append(
            "Collaborative learning sessions"
        )

    elif persona == "Burnout Pattern":

        recommendations.append(
            "Reduced workload planning"
        )

        recommendations.append(
            "Mental wellness support"
        )

    elif persona == "Erratic Learner":

        recommendations.append(
            "Structured daily study planner"
        )

    # =====================================
    # RISK-BASED
    # =====================================

    if risk == "Critical Risk":

        recommendations.append(
            "Immediate faculty mentoring"
        )

    elif risk == "High Risk":

        recommendations.append(
            "Weekly intervention monitoring"
        )

    return recommendations