def analyze_video_behavior(student):

    # =====================================
    # ATTENTION SCORE
    # =====================================

    attention_score = 100

    attention_score -= (
        student.pause_count * 2
    )

    attention_score -= (
        student.rewind_count * 1.5
    )

    attention_score -= (
        student.tab_switches * 5
    )

    attention_score -= (
        student.inactivity_time * 0.5
    )

    attention_score = max(
        0,
        attention_score
    )

    # =====================================
    # CONFUSION SCORE
    # =====================================

    confusion_score = (
        student.pause_count * 2
        +
        student.rewind_count * 3
    )

    # =====================================
    # LEARNING STATUS
    # =====================================

    if confusion_score > 40:

        learning_status = (
            "High Confusion Detected"
        )

    elif confusion_score > 20:

        learning_status = (
            "Moderate Confusion"
        )

    else:

        learning_status = (
            "Stable Learning Behaviour"
        )

    return {

        "attention_score": attention_score,

        "confusion_score": confusion_score,

        "learning_status": learning_status
    }