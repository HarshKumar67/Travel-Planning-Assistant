from llm import generate_response

class ItineraryAgent:

    def run(self, research_data):

        prompt = f"""
        You are a Travel Itinerary Planning Agent.

        Based on the following travel research:

        {research_data}

        Create a detailed day-wise itinerary.

        Requirements:
        - Create plans for each day
        - Include attractions
        - Include food suggestions
        - Include activities
        - Keep it realistic and budget-friendly
        - Maintain good travel flow

        Return the result in a clean structured format.
        """

        response = generate_response(prompt)

        return response