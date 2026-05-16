from llm import generate_response

class ResearchAgent:

    def run(self, intent_data):

        prompt = f"""
        You are a Travel Research Agent.

        Based on the following travel details:

        {intent_data}

        Provide:
        - destination overview
        - famous attractions
        - weather information
        - best places to visit
        - recommended activities
        - travel tips

        Return the result in a clean structured format.
        """

        response = generate_response(prompt)

        return response