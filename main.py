from agent.marketing_agent import run_campaign

if __name__ == "__main__":
    result = run_campaign(
        product="EcoBottle",
        audience="young professionals",
        tone="bold",
        content_type="Instagram ad",
    )
    print("\nGenerated Campaign:\n", result)
