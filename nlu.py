def detect_intent(text):
    t = text.lower()
    if "weather" in t or "forecast" in t:
        return "get_weather"
    if "remind" in t or "reminder" in t:
        return "set_reminder"
    return "general_qa"
