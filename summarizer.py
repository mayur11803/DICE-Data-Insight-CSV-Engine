import os
from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOllama

# ✅ Load LLaMA model from Ollama
llm = ChatOllama(model="llama3", temperature=0.3)

# ✅ Define the summarization prompt
summary_prompt = PromptTemplate(
    input_variables=["stats", "sample"],
    template="""
    You are a data analysis assistant. Given the following dataset statistics and a small sample of the data,
    write a concise, insightful executive summary for business stakeholders.

    Focus on interesting trends, patterns, or customer behaviors.

    --- STATS ---
    {stats}

    --- SAMPLE DATA ---
    {sample}

    --- EXECUTIVE SUMMARY ---
    """
)

# ✅ Create a chain using LLaMA and the prompt
summarizer_chain = LLMChain(llm=llm, prompt=summary_prompt)

# ✅ Main agent function used in LangGraph
def summarizer_agent(df, stats):
    # Convert top rows of dataframe to a markdown table (clean + readable)
    sample = df.head().to_markdown(index=False)
    return summarizer_chain.run(stats=stats, sample=sample)

