from agents.intent_agent import IntentAgent
from agents.research_agent import ResearchAgent
from agents.itinerary_agent import ItineraryAgent
from agents.budget_agent import BudgetAgent


class OrchestratorAgent:

    def __init__(self):

        self.intent_agent = IntentAgent()
        self.research_agent = ResearchAgent()
        self.itinerary_agent = ItineraryAgent()
        self.budget_agent = BudgetAgent()

    def run(self, user_input, memory_context=""):
        enhanced_input = f"""
        Previous Conversation History:
        {memory_context}

        Current User Request:
        {user_input}

        """

        # STEP 1 → Intent Agent
        intent_result = self.intent_agent.run(enhanced_input)

        # STEP 2 → Research Agent
        research_result = self.research_agent.run(intent_result)

        # STEP 3 → Itinerary Agent
        itinerary_result = self.itinerary_agent.run(research_result)

        # STEP 4 → Budget Agent
        budget_result = self.budget_agent.run(itinerary_result)

        # FINAL RESPONSE
        final_output = f"""

# AI Travel Plan

## User Request
{user_input}

---

## Destination Analysis
{intent_result}

---

## Destination Research
{research_result}

---

## Day-Wise Itinerary
{itinerary_result}

---

## Budget Estimation
{budget_result}

"""

        return final_output