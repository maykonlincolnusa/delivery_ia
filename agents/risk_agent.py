from crewai.tools import tool

@tool
def risk_tool(deliveries: list) -> str:
    risky = [
        d for d in deliveries
        if d["status"] == "delayed" and d["eta_minutes"] > 30
    ]

    if not risky:
        return "No operational risks detected"

    return f"{len(risky)} high-risk deliveries detected"
