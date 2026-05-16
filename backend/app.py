from fastapi import FastAPI

import pandas as pd
import joblib

# =========================================
# SCHEMA
# =========================================

from schemas.student_schema import StudentData

# =========================================
# SERVICES
# =========================================

from services.video_analytics_service import (
    analyze_video_behavior
)

from services.attention_service import (
    calculate_attention_risk
)

from services.genai_service import (
    generate_ai_summary
)

from services.recommendation_service import (
    recommend_resources
)

# =========================================
# LOAD MODELS
# =========================================

xgb_model = joblib.load(
    "../models/xgboost_model.pkl"
)

scaler = joblib.load(
    "../models/feature_scaler.pkl"
)

kmeans = joblib.load(
    "../models/persona_kmeans.pkl"
)

persona_scaler = joblib.load(
    "../models/persona_scaler.pkl"
)

# =========================================
# FASTAPI INIT
# =========================================

app = FastAPI()

# =========================================
# PERSONA LABELS
# =========================================

persona_map = {

    0: "Consistent Learner",

    1: "Burnout Pattern",

    2: "Silent Isolator",

    3: "Erratic Learner"
}

# =========================================
# INTERVENTION ENGINE
# =========================================

def recommend_intervention(persona, risk):

    if risk == "Critical Risk":

        if persona == "Burnout Pattern":

            return (
                "Mental health counseling "
                "+ workload reduction"
            )

        elif persona == "Silent Isolator":

            return (
                "Peer mentoring + "
                "social engagement support"
            )

        elif persona == "Erratic Learner":

            return (
                "Personal academic advisor "
                "intervention"
            )

        else:

            return (
                "Immediate faculty monitoring"
            )

    elif risk == "High Risk":

        return "Faculty mentoring"

    elif risk == "Medium Risk":

        return "Engagement reminders"

    else:

        return (
            "No major intervention required"
        )

# =========================================
# HOME ROUTE
# =========================================

@app.get("/")
def home():

    return {

        "message":
        "EduGuard-AI Backend Running"
    }

# =========================================
# MAIN AI ROUTE
# =========================================

@app.post("/predict")
def predict(student: StudentData):

    # =====================================
    # CONVERT INPUT
    # =====================================

    data = pd.DataFrame([{

        "code_module":
        student.code_module,

        "code_presentation":
        student.code_presentation,

        "gender":
        student.gender,

        "region":
        student.region,

        "highest_education":
        student.highest_education,

        "imd_band":
        student.imd_band,

        "age_band":
        student.age_band,

        "num_of_prev_attempts":
        student.num_of_prev_attempts,

        "studied_credits":
        student.studied_credits,

        "disability":
        student.disability,

        "date_registration":
        student.date_registration,

        "total_clicks":
        student.total_clicks,

        "total_active_days":
        student.total_active_days,

        "avg_clicks_per_day":
        student.avg_clicks_per_day,

        "forum_clicks":
        student.forum_clicks,

        "resource_clicks":
        student.resource_clicks,

        "activity_diversity":
        student.activity_diversity,

        "disengagement_streak":
        student.disengagement_streak,

        "early_late_ratio":
        student.early_late_ratio,

        "engagement_volatility":
        student.engagement_volatility,

        "peak_to_trough_ratio":
        student.peak_to_trough_ratio
    }])

    # =====================================
    # SCALE FEATURES
    # =====================================

    scaled_data = scaler.transform(data)

    # =====================================
    # RISK PREDICTION
    # =====================================

    probability = (
        xgb_model
        .predict_proba(scaled_data)[0][1]
    )

    # =====================================
    # RISK CATEGORY
    # =====================================

    if probability < 0.30:

        risk = "Low Risk"

    elif probability < 0.60:

        risk = "Medium Risk"

    elif probability < 0.80:

        risk = "High Risk"

    else:

        risk = "Critical Risk"

    # =====================================
    # PERSONA PREDICTION
    # =====================================

    persona_features = data[
        [
            'total_clicks',
            'total_active_days',
            'forum_clicks',
            'activity_diversity',
            'disengagement_streak',
            'engagement_volatility'
        ]
    ]

    scaled_persona = (
        persona_scaler
        .transform(persona_features)
    )

    cluster = (
        kmeans
        .predict(scaled_persona)[0]
    )

    persona = persona_map[cluster]

    # =====================================
    # INTERVENTION
    # =====================================

    intervention = (
        recommend_intervention(
            persona,
            risk
        )
    )

    # =====================================
    # VIDEO ANALYTICS
    # =====================================

    video_analysis = (
        analyze_video_behavior(student)
    )

    # =====================================
    # ATTENTION ENGINE
    # =====================================

    attention_analysis = (
        calculate_attention_risk(student)
    )

    # =====================================
    # RESOURCE RECOMMENDER
    # =====================================

    recommendations = (
        recommend_resources(

            risk,

            persona,

            video_analysis[
                "confusion_score"
            ]
        )
    )

    # =====================================
    # GENAI SUMMARY
    # =====================================

    ai_summary = (
        generate_ai_summary(

            risk,

            persona,

            intervention,

            attention_analysis[
                "attention_label"
            ],

            video_analysis[
                "learning_status"
            ]
        )
    )

    # =====================================
    # FINAL RESPONSE
    # =====================================

    return {

        "risk_probability":
        float(probability),

        "risk_category":
        risk,

        "student_persona":
        persona,

        "recommended_intervention":
        intervention,

        "video_analytics":
        video_analysis,

        "attention_analysis":
        attention_analysis,

        "recommended_resources":
        recommendations,

        "ai_generated_summary":
        ai_summary
    }