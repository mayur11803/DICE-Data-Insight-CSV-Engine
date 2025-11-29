# 📊 ADA – Autonomous CSV Insight Generator

**ADA** (Autonomous Data Analyst) is a multi-agent LangGraph application that automatically analyzes CSV datasets and generates a polished `.docx` report with executive summaries, statistical insights, and visual charts — powered by local LLMs via [Ollama](https://ollama.com/).

> Built with LangGraph, Streamlit, LLaMA3, and Python.

---

## ✨ Features

- 🔍 **Automatic Data Cleaning**
- 📈 **Descriptive Statistics**
- 🧠 **Executive Summary Generation** (via LLaMA3)
- 📊 **Chart Generation** (Matplotlib)
- 📄 **Formatted DOCX Report Output**
- 🤖 **Fully Local Execution** (no OpenAI key needed)

---

## 📁 File Structure

CSV_Insight_Generator/
├── app.py # Streamlit UI
├── workflows/
│ └── graph.py # LangGraph multi-step pipeline
├── agents/
│ ├── cleaner.py # Cleans and loads CSV
│ ├── analyzer.py # Computes stats
│ ├── summarizer.py # Uses LLM to write summary
│ ├── grapher.py # Generates and saves charts
│ └── writer.py # Builds DOCX report
├── utils/
│ └── init.py # (optional utility folder)
├── requirements.txt
└── README.md


---

## 🚀 Getting Started

### 1. Install [Ollama](https://ollama.com/download)

```bash
ollama pull llama3
```

### 2. Clone and Set Up:
```bash
git clone https://github.com/yourusername/CSV_Insight_Generator.git
cd CSV_Insight_Generator
pip install -r requirements.txt
```

### 3. Run the App:
```bash
streamlit run app.py
```

🧠 How It Works
The app uses LangGraph to define a multi-step pipeline:

Cleaner Agent → Loads & cleans the uploaded CSV

Analyzer Agent → Computes mean, median, std, etc.

Summarizer Agent → Sends stats + data sample to LLaMA3 for summary

Grapher Agent → Saves histogram/box plots

Writer Agent → Assembles everything into a .docx report

⚙️ Tech Stack
🧠 LangGraph (workflow orchestration)

🗂️ Pandas + Matplotlib

📝 Python docx for report generation

🧠 Ollama + LLaMA3 for offline LLM

🌐 Streamlit UI

📦 Requirements
txt
Copy
Edit
streamlit
pandas
matplotlib
python-docx
langchain
langgraph
langchain-community
ollama

📜 License
MIT License. Feel free to use, share, and build upon it!

