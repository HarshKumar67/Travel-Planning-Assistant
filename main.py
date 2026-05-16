from agents.orchestrator import OrchestratorAgent

print("Starting AI Travel Planning System...\n")

orchestrator = OrchestratorAgent()

user_input = input("Enter your travel request:\n")

final_result = orchestrator.run(user_input)

print(final_result)

print("\nSystem Executed Successfully!")