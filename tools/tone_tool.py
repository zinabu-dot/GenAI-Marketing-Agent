def adapt_tone(text: str, brand_voice: str = "friendly") -> str:
    if brand_voice == "friendly":
        return f"Hey there! 😊 Just a quick heads-up: {text}"
    elif brand_voice == "professional":
        return f"Please note: {text}"
    elif brand_voice == "bold":
        return f"🔥 Hot Take: {text.upper()}"
    return text
