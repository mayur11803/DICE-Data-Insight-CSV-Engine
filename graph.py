from langgraph.graph import StateGraph
from typing import TypedDict, Any
from agents.cleaner import cleaner_agent
from agents.analyzer import analyzer_agent
from agents.summarizer import summarizer_agent
from agents.grapher import grapher_agent
from agents.writer import report_writer

class CSVState(TypedDict):
    file: bytes
    df: Any
    stats: str
    summary: str
    charts: list
    docx: Any

# Agent steps
def run_cleaner(state: CSVState) -> CSVState:
    df = cleaner_agent(state["file"])
    return {**state, "df": df}

def run_analyzer(state: CSVState) -> CSVState:
    stats = analyzer_agent(state["df"])
    return {**state, "stats": stats}

def run_summarizer(state: CSVState) -> CSVState:
    summary = summarizer_agent(state["df"], state["stats"])
    return {**state, "summary": summary}

def run_grapher(state: CSVState) -> CSVState:
    charts = grapher_agent(state["df"])
    return {**state, "charts": charts}

def generate_report(state: CSVState) -> dict:
    try:
        docx_buffer = report_writer(
            df=state["df"],
            stats=state["stats"],
            summary=state["summary"],
            charts=state.get("charts", [])
        )

        return {
            "summary": state["summary"],
            "docx": docx_buffer
        }
    except Exception as e:
        print(f"[ERROR in generate_report]: {e}")
        return {"summary": state["summary"]}

def run_csv_analysis(file_bytes: bytes):
    builder = StateGraph(CSVState)

    builder.add_node("clean", run_cleaner)
    builder.add_node("analyze", run_analyzer)
    builder.add_node("summarize", run_summarizer)
    builder.add_node("graph", run_grapher)
    builder.add_node("write", generate_report)

    builder.set_entry_point("clean")
    builder.add_edge("clean", "analyze")
    builder.add_edge("analyze", "summarize")
    builder.add_edge("summarize", "graph")
    builder.add_edge("graph", "write")

    builder.set_finish_point("write")  # ✅ this is required

    graph = builder.compile()
    return graph.invoke({"file": file_bytes})
