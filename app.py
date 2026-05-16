import streamlit as st
from agents.orchestrator import OrchestratorAgent
import time

# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# ==============================
# MEMORY INITIALIZATION
# ==============================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ==============================
# CUSTOM CSS
# ==============================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stTextArea textarea {
    font-size: 16px;
}

.big-title {
    font-size: 42px;
    font-weight: bold;
    color: #4FC3F7;
}

.sub-title {
    font-size: 18px;
    color: #CCCCCC;
}

.section-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #1E1E1E;
    margin-bottom: 20px;
    border: 1px solid #333333;
}

.footer-text {
    text-align: center;
    color: gray;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# SIDEBAR
# ==============================

st.sidebar.title("✈️ AI Travel Planner")

st.sidebar.markdown("---")

st.sidebar.info(
    """
This project uses a **Multi-Agent AI Architecture**.

### Agents Used:
- Intent Agent
- Research Agent
- Itinerary Agent
- Budget Agent
- Orchestrator Agent
"""
)

st.sidebar.markdown("---")

st.sidebar.success("Built for Hiring Assignment 🚀")

# ==============================
# HEADER
# ==============================

st.markdown(
    '<div class="big-title">🌍 AI Travel Planning Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Plan complete trips using an End-to-End Multi-Agent AI System</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# ==============================
# USER INPUT
# ==============================

user_input = st.text_area(
    "🧳 Enter Your Travel Request",
    placeholder="Example: Plan a 5-day Goa trip under ₹20,000 for 2 friends who love beaches and nightlife",
    height=150
)

# ==============================
# GENERATE BUTTON
# ==============================

if st.button("🚀 Generate Travel Plan"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter a travel request.")

    else:

        with st.spinner("🤖 AI Agents are planning your trip..."):

            orchestrator = OrchestratorAgent()

            # Build memory context

            memory_context = ""

            for chat in st.session_state.chat_history:

                memory_context += f"""
            User: {chat['user']}

            AI Response:
            {chat['response']}
            """

            # Generate final result with memory

            final_result = orchestrator.run(
                user_input,
                memory_context
            )
        
        # Save conversation in memory

        st.session_state.chat_history.append({
                "user": user_input,
                "response": final_result
                })

        st.success("✅ Travel Plan Generated Successfully!")

        st.markdown("---")

        # ==============================
        # OUTPUT SECTION
        # ==============================

        st.markdown("""
        <div class="section-box">
        <h2>📋 Complete Travel Plan</h2>
        </div>
        """, unsafe_allow_html=True)

        # Expandable Output
        with st.expander("🌍 View Full AI Travel Plan", expanded=True):

            output_placeholder = st.empty()

            streamed_text = ""

            for char in final_result:

                streamed_text += char

                output_placeholder.markdown(streamed_text)

                time.sleep(0.001)

# ==============================
# SAMPLE PROMPTS
# ==============================

st.markdown("---")

st.subheader("✨ Example Travel Requests")

col1, col2 = st.columns(2)

with col1:

    st.info("""
    🏖️ Plan a 5-day Goa trip under ₹20,000 for 2 friends who love beaches and nightlife
    """)

    st.info("""
    🏔️ Plan a 4-day Manali adventure trip under ₹15,000
    """)

with col2:

    st.info("""
    🕌 Plan a luxury Jaipur heritage trip for a couple
    """)

    st.info("""
    🌴 Plan a budget Kerala trip with nature and boating activities
    """)

# ==============================
# FOOTER
# ==============================

st.markdown("---")

st.markdown(
    '<div class="footer-text">Built using Multi-Agent AI • Streamlit • Groq LLM 🚀</div>',
    unsafe_allow_html=True
)


# ==============================
# CONVERSATION HISTORY
# ==============================

if st.session_state.chat_history:

    st.markdown("---")
    st.subheader("🧠 Conversation Memory")

    for chat in reversed(st.session_state.chat_history):

        with st.expander(f"🧳 {chat['user'][:60]}"):

            st.markdown(chat["response"])