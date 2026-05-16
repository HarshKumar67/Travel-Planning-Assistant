from agents.intent_agent import IntentAgent
from agents.research_agent import ResearchAgent

print("Starting Program...")

# Create agents
intent_agent = IntentAgent()
research_agent = ResearchAgent()

# User input
user_input = "Plan a 5-day Goa trip under ₹20,000 for 2 friends who love beaches and nightlife"

# Step 1 → Intent Agent
intent_result = intent_agent.run(user_input)

print("\n===== INTENT AGENT OUTPUT =====\n")
print(intent_result)

# Step 2 → Research Agent
research_result = research_agent.run(intent_result)

print("\n===== RESEARCH AGENT OUTPUT =====\n")
print(research_result)

print("\nProgram Finished Successfully!")