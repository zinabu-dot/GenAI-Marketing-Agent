def seo_score(text: str) -> str:
    keywords = ["engagement", "growth", "audience", "click", "conversion"]
    score = sum(1 for k in keywords if k in text.lower())
    return f"SEO Score: {score}/5 — {'Good' if score >= 3 else 'Needs Improvement'}"
