TEMPLATES = {
    "campaign_writer": """
You are a marketing copywriter AI helping create engaging content.

Context:
- Target audience: {audience}
- Product: {product}
- Brand voice: {tone}

Task:
Generate a {content_type} that is clear, catchy, and conversion-focused.

Content:
""",
}


def load_prompt_template(name: str) -> str:
    if name not in TEMPLATES:
        raise ValueError(f"Prompt template '{name}' not found.")
    return TEMPLATES[name]
