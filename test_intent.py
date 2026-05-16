from agents.intent_agent import IntentAgent

agent = IntentAgent()

response = agent.run(
    "Plan a 5-day Goa trip under ₹20,000 for 2 friends who love beaches and nightlife"
)

print(response)