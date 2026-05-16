from pydantic import BaseModel

class StudentData(BaseModel):

    code_module: int
    code_presentation: int
    gender: int
    region: int
    highest_education: int
    imd_band: int
    age_band: int
    num_of_prev_attempts: int
    studied_credits: int
    disability: int

    date_registration: float

    total_clicks: float
    total_active_days: float
    avg_clicks_per_day: float

    forum_clicks: float
    resource_clicks: float
    activity_diversity: float

    disengagement_streak: float
    early_late_ratio: float
    engagement_volatility: float
    peak_to_trough_ratio: float

    # =====================================
    # NOVEL VIDEO ANALYTICS FEATURES
    # =====================================

    watch_duration: float = 0
    pause_count: int = 0
    rewind_count: int = 0
    tab_switches: int = 0
    inactivity_time: float = 0