from agents.intent_agent import IntentAgent
from agents.research_agent import ResearchAgent
from agents.itinerary_agent import ItineraryAgent
from agents.budget_agent import BudgetAgent

print("Starting AI Travel Planner...\n")

# Create agents
intent_agent = IntentAgent()
research_agent = ResearchAgent()
itinerary_agent = ItineraryAgent()
budget_agent = BudgetAgent()

# User input
user_input = "Plan a 5-day Goa trip under ₹20,000 for 2 friends who love beaches and nightlife"

# STEP 1 → Intent Agent
intent_result = intent_agent.run(user_input)

print("===== INTENT AGENT OUTPUT =====\n")
print(intent_result)

# STEP 2 → Research Agent
research_result = research_agent.run(intent_result)

print("\n===== RESEARCH AGENT OUTPUT =====\n")
print(research_result)

# STEP 3 → Itinerary Agent
itinerary_result = itinerary_agent.run(research_result)

print("\n===== ITINERARY AGENT OUTPUT =====\n")
print(itinerary_result)

# STEP 4 → Budget Agent
budget_result = budget_agent.run(itinerary_result)

print("\n===== BUDGET AGENT OUTPUT =====\n")
print(budget_result)

print("\nAI Travel Planner Executed Successfully!")