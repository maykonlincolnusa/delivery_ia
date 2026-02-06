from crewai import Agent, Task, Crew
from agents.monitor_agent import monitor_tool
from agents.support_agent import support_tool
from agents.risk_agent import risk_tool

def run_crew(data):

    monitor_agent = Agent(
        role="Monitoring Agent",
        goal="Monitor delivery status",
        tools=[monitor_tool],
        verbose=True
    )

    support_agent = Agent(
        role="Support Agent",
        goal="Prioritize support tickets",
        tools=[support_tool],
        verbose=True
    )

    risk_agent = Agent(
        role="Risk Agent",
        goal="Detect operational anomalies",
        tools=[risk_tool],
        verbose=True
    )

    tasks = [
        Task(description="Monitor deliveries", agent=monitor_agent),
        Task(description="Analyze support tickets", agent=support_agent),
        Task(description="Detect risks", agent=risk_agent),
    ]

    crew = Crew(
        agents=[monitor_agent, support_agent, risk_agent],
        tasks=tasks
    )

    crew.kickoff(inputs=data)
