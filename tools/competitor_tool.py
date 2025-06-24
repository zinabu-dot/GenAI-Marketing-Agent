def analyze_competitor(product_name: str) -> str:
    fake_db = {
        "ProductX": "CompetitorX is focusing on TikTok growth and influencer outreach.",
        "ProductY": "CompetitorY just launched an AI-driven email campaign tool.",
    }
    return fake_db.get(product_name, "No recent activity found for that competitor.")
