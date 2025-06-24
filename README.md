# GenAI Marketing Agent

A modular generative AI-powered agent designed to assist with automated marketing tasks such as SEO analysis, content tone adjustment, and competitor research. Built with [LangChain](https://www.langchain.com/), [Hugging Face Hub](https://huggingface.co/), and custom tools, this project enables users to generate and refine marketing campaigns dynamically.

---

## 🧠 Features

- 🔍 **SEO Optimization** — Suggests SEO strategies based on content input.
- 🗣️ **Tone Adjustment** — Adjusts text tone (e.g., formal, friendly, persuasive).
- 🕵️ **Competitor Research** — Generates market insights from simulated competitor queries.
- ⚙️ Modular architecture with agent-based reasoning and tool usage.

---

## 📁 Project Structure

genai-marketing-agent/
│
├── main.py # Entry point to run the marketing agent
├── agent/
│ └── marketing_agent.py # Core agent definition and orchestration
├── prompts/
│ └── templates.py # Prompt templates for consistent generation
├── tools/
│ ├── seo_tool.py # SEO recommendation logic
│ ├── tone_tool.py # Text tone modification utility
│ └── competitor_tool.py # Competitor analysis mockup
├── requirements.txt # Python package dependencies
├── README.md # This documentation file


---

## 🚀 Getting Started

### 1. Clone the Repository

```
git clone https://github.com/zinabu-dot/GenAI-Marketing-Agent.git
cd GenAI-Marketing-Agent
```

### 2. Set Up a Virtual Environment

```
python -m venv venv
source venv/bin/activate          # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Set Your HuggingFace API Token
Set your Hugging Face token in your shell environment:

```
export HUGGINGFACEHUB_API_TOKEN=your_token_here   # macOS/Linux
set HUGGINGFACEHUB_API_TOKEN=your_token_here      # Windows CMD
$env:HUGGINGFACEHUB_API_TOKEN="your_token_here"   # PowerShell
Alternatively, you can create a .env file and load it using python-dotenv.
```

🏃 Run the Agent

```
python main.py
```

The agent will prompt you to describe your marketing goal and will generate a detailed marketing campaign using the integrated tools.

🛠 Tools
Tool	Description
seo_tool.py	Provides SEO improvement suggestions based on the input.
tone_tool.py	Alters the tone of the content (e.g., formal, playful).
competitor_tool.py	Simulates basic competitor analysis with example data.

🔄 Model Compatibility
This project currently supports:

✅ Hugging Face LLMs via HuggingFaceEndpoint

❌ Not compatible with AgentType.OPENAI_FUNCTIONS (use ZERO_SHOT_REACT_DESCRIPTION instead)

To use OpenAI LLMs instead, change the agent initialization and set OPENAI_API_KEY.

📚 Roadmap
 Migrate to LangGraph for advanced workflows

 Add UI via Streamlit or Gradio

 Integrate real web scraping for live competitor data

📄 License
This project is open-source and available under the MIT License.

🙌 Acknowledgments
- LangChain

- Hugging Face Transformers