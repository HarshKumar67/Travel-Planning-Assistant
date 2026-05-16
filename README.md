# ✈️ AI Travel Planning Assistant

An End-to-End Multi-Agent AI Travel Planner built using Streamlit, Groq LLM, and modular AI agents.

This project generates personalized travel plans by coordinating multiple AI agents responsible for:
- intent understanding
- travel research
- itinerary generation
- budget estimation

The system also supports:
- conversational memory
- weather API integration
- streaming responses
- interactive web UI

---

# 🚀 Features

✅ Multi-Agent AI Architecture  
✅ Intent Understanding Agent  
✅ Travel Research Agent  
✅ Itinerary Planning Agent  
✅ Budget Estimation Agent  
✅ Orchestrator Agent  
✅ Conversational Memory   
✅ Streaming Responses  
✅ Interactive Streamlit UI  

---

# 🧠 Architecture Diagram

```text
                    USER INPUT
                         ↓
               ORCHESTRATOR AGENT
                         ↓
                 Intent Agent
                         ↓
                Research Agent
                         ↓
               Itinerary Agent
                         ↓
                 Budget Agent
                         ↓
                   FINAL OUTPUT
```

---

# ⚙️ Agent Workflow

## 1️⃣ Intent Agent
Extracts:
- destination
- budget
- duration
- travel preferences

### Example:
Input:
"Plan a 5-day Goa trip under ₹20,000"

Output:
- Destination: Goa
- Budget: ₹20,000
- Duration: 5 Days

---

## 2️⃣ Research Agent
Collects:
- destination information
- attractions
- weather details
- activities
- travel tips


---

## 3️⃣ Itinerary Agent
Creates:
- day-wise travel plan
- attraction schedule
- activity planning
- food recommendations

---

## 4️⃣ Budget Agent
Estimates:
- hotel expenses
- food expenses
- travel expenses
- activity expenses
- total estimated budget

---

## 5️⃣ Orchestrator Agent
Coordinates all agents and manages:
- workflow execution
- inter-agent communication
- final response generation

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- Llama 3.1 8B Instant
- Requests
- dotenv

---

# 📂 Project Structure

```text
TRAVEL_AI_ASSISTANT/

│
├── agents/
│   ├── app.py
│   ├── budget_agent.py
│   ├── intent_agent.py
│   ├── itinerary_agent.py
│   ├── orchestrator.py
│   └── research_agent.py
│
├── venv/
│
├── .env
├── .gitignore
├── app.py
├── llm.py
├── main.py
├── README.md
├── requirements.txt
├── test_budget.py
├── test_gemini.py
├── test_intent.py
├── test_itinerary.py
└── test_research.py
```

---

# ⚡ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone YOUR_GITHUB_REPO_LINK
```

---

## 2️⃣ Open Project Folder

```bash
cd travel_ai_assistant
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Add Environment Variables

Create a `.env` file and add:

```env
GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_weather_api_key
```

---

## 6️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

# 🧪 Sample Input

```text
Plan a 4-day Manali adventure trip under ₹15,000 for 2 friends who love trekking and snow activities
```

---

# ✅ Sample Output

```text
Destination: Manali

Weather:
Temperature: 12°C
Weather: Snowy

Day 1:
- Arrival
- Mall Road Visit
- Local Cafe Exploration

Day 2:
- Solang Valley
- Adventure Sports
- Ropeway Experience

Estimated Budget:
₹14,500
```

---

# 🔮 Future Improvements

- Flight API Integration
- Hotel Recommendation System
- Real-time Google Maps Integration
- Voice-based Travel Planning
- Multi-language Support

---

# 🌐 Deployment

[Deployment link of the project.](https://travel-planning-assistant-gnlpsscravcddm6uy98opj.streamlit.app/)

---

# 👨‍💻 Author

Harsh Kumar
