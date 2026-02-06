from crewai.tools import tool

@tool
def support_tool(data: dict) -> str:
    deliveries = data["deliveries"]
    tickets = data["tickets"]

    alerts = []

    for ticket in tickets:
        for delivery in deliveries:
            if (
                ticket["delivery_id"] == delivery["delivery_id"]
                and delivery["status"] == "delayed"
            ):
                alerts.append(
                    f"Ticket {ticket['ticket_id']} escalated due to delayed delivery {delivery['delivery_id']}"
                )

    return "\n".join(alerts) if alerts else "No critical support issues"
