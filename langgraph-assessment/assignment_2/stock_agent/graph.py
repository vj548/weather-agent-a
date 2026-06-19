from langgraph.graph import StateGraph, END
from .state import StockAgentState
from .nodes import fetch_data, calculate_indicators, generate_recommendation, format_report

def route_error(state: StockAgentState) -> str:
    if state.get("error"):
        return "format_report"
    return "calculate_indicators"

builder = StateGraph(StockAgentState)
builder.add_node("fetch_data", fetch_data)
builder.add_node("calculate_indicators", calculate_indicators)
builder.add_node("generate_recommendation", generate_recommendation)
builder.add_node("format_report", format_report)

builder.set_entry_point("fetch_data")
builder.add_conditional_edges(
    "fetch_data",
    route_error,
    {
        "calculate_indicators": "calculate_indicators",
        "format_report": "format_report"
    }
)
builder.add_edge("calculate_indicators", "generate_recommendation")
builder.add_edge("generate_recommendation", "format_report")
builder.add_edge("format_report", END)

stock_agent_app = builder.compile()
