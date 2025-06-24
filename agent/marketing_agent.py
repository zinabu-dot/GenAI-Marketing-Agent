import os
from langchain.agents import Tool, initialize_agent
from prompts.templates import load_prompt_template
from tools.seo_tool import seo_score
from tools.tone_tool import adapt_tone
from tools.competitor_tool import analyze_competitor

from langchain.agents.agent_types import AgentType
from langchain_huggingface import HuggingFaceEndpoint

from dotenv import load_dotenv

load_dotenv()


# Initialize Hugging Face LLM (replace with your own HF token)
llm = HuggingFaceEndpoint(
    endpoint_url="https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3",
    # "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    temperature=0.2,
    max_new_tokens=512,
    repetition_penalty=1.03,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)


seo = Tool(
    name="SEOCheck",
    func=seo_score,
    description="Evaluates SEO quality of marketing text.",
)
tone = Tool(
    name="ToneAdapter",
    func=adapt_tone,
    description="Adapts content tone to brand voice.",
)
competitor = Tool(
    name="CompetitorIntel",
    func=analyze_competitor,
    description="Gives insights on product competitors.",
)

# Initialize agent with tools
agent = initialize_agent(
    tools=[seo, tone, competitor],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)


def run_campaign(product: str, audience: str, tone: str, content_type: str):
    template = load_prompt_template("campaign_writer")
    prompt = template.format(
        product=product, audience=audience, tone=tone, content_type=content_type
    )
    return agent.run(prompt)
