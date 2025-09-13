def run(user_data: dict = None):
    if not user_data:
        user_data = {}

    # Mock logic: recommend based on "level" key if it exists
    level = user_data.get("level", "beginner").lower()

    if level == "beginner":
        return {"recommendations": ["Yoga 101", "Intro to Breathwork"]}
    elif level == "intermediate":
        return {"recommendations": ["Dynamic Flow", "Core Stability"]}
    elif level == "advanced":
        return {"recommendations": ["Ashtanga Series", "Kundalini Intensive"]}
    else:
        return {"recommendations": ["General Wellness Track", "Meditation Basics"]}
