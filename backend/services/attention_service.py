def calculate_attention_risk(student):

    risk_score = 0

    # =====================================
    # BEHAVIOURAL FACTORS
    # =====================================

    risk_score += (
        student.disengagement_streak * 1.5
    )

    risk_score += (
        student.engagement_volatility * 1.2
    )

    # =====================================
    # VIDEO FACTORS
    # =====================================

    risk_score += (
        student.tab_switches * 3
    )

    risk_score += (
        student.inactivity_time * 0.8
    )

    # =====================================
    # NORMALIZATION
    # =====================================

    attention_risk = min(
        100,
        round(risk_score, 2)
    )

    # =====================================
    # LABEL
    # =====================================

    if attention_risk > 80:

        label = "Critical Attention Risk"

    elif attention_risk > 50:

        label = "High Attention Risk"

    elif attention_risk > 25:

        label = "Moderate Attention Risk"

    else:

        label = "Low Attention Risk"

    return {

        "attention_risk_score": attention_risk,

        "attention_label": label
    }