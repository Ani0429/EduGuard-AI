def generate_ai_summary(

    risk,

    persona,

    intervention,

    attention_label,

    learning_status
):

    # =====================================
    # LOW RISK
    # =====================================

    if risk == "Low Risk":

        summary = f"""

Student currently shows stable academic behaviour.

The learner belongs to the
'{persona}' category.

Video engagement patterns indicate:
'{learning_status}'.

Current attention analysis:
'{attention_label}'.

No immediate intervention is required,
but continued engagement monitoring
is recommended.

"""

    # =====================================
    # MEDIUM RISK
    # =====================================

    elif risk == "Medium Risk":

        summary = f"""

Student shows moderate academic risk.

Behavioural persona identified:
'{persona}'.

Attention analytics indicate:
'{attention_label}'.

Learning behaviour suggests:
'{learning_status}'.

Recommended actions:
- Encourage forum participation
- Increase peer interaction
- Provide structured revision plans

"""

    # =====================================
    # HIGH RISK
    # =====================================

    elif risk == "High Risk":

        summary = f"""

Student shows high academic risk
with declining engagement patterns.

Detected persona:
'{persona}'.

Attention monitoring reports:
'{attention_label}'.

Learning analytics identified:
'{learning_status}'.

Recommended interventions:
- Faculty mentoring
- Personalized learning support
- Adaptive learning resources
- Weekly progress tracking

"""

    # =====================================
    # CRITICAL RISK
    # =====================================

    else:

        summary = f"""

Critical academic risk detected.

Student persona:
'{persona}'.

Attention intelligence status:
'{attention_label}'.

Learning analysis result:
'{learning_status}'.

URGENT recommended actions:
- Immediate faculty intervention
- Mental health and academic counseling
- Personalized recovery plan
- Parent or mentor communication
- Intensive engagement monitoring

"""

    return summary