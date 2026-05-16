from llm import generate_response

class BudgetAgent:

    def run(self, itinerary_data):

        prompt = f"""
        You are a Travel Budget Estimation Agent.

        Based on the following travel itinerary:

        {itinerary_data}

        Estimate:
        - hotel expenses
        - travel expenses
        - food expenses
        - activity expenses
        - miscellaneous expenses

        Also provide:
        - total estimated budget
        - budget-saving tips

        Keep the estimates realistic and budget-friendly.

        Return the result in a clean structured format.
        """

        response = generate_response(prompt)

        return response