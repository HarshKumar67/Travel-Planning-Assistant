from llm import generate_response

class IntentAgent:

    def run(self, user_input):

        prompt = f"""
        You are an Intent Understanding Agent.

        Extract the following details from the user input:
        - Destination
        - Budget
        - Duration
        - Preferences

        User Input:
        {user_input}

        Return the result in a clean structured format.
        """

        response = generate_response(prompt)

        return response