import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Icebreaker Quest 🎲", page_icon="❄️", layout="centered")

# --- Custom CSS for styling ---
st.markdown("""
    <style>
    html, body, [class*="css"] {
        background-color: #FAF3F0;
        color: black;
        font-family: 'Segoe UI', sans-serif;
    }
    .question-box {
        background-color: #E6E6FA;
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #B39DDB;
        margin-top: 20px;
        color: black;
    }
    .answer-box {
        background-color: #FFE4E1;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #D8BFD8;
        margin-top: 15px;
        box-shadow: 1px 1px 8px #D8BFD8;
        color: black;
    }
    .center {
        text-align: center;
    }
    .stTextArea textarea {
        background-color: #FFF8E7;
        color: black;
        border: 1px solid #D8BFD8;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 class='center'>🎀 Icebreaker Quest</h1>", unsafe_allow_html=True)
st.markdown("<p class='center'>Break the ice with aesthetic vibes and black text elegance 🖤</p>", unsafe_allow_html=True)

# --- Question list ---
questions = [
    "🌟 What’s your full name or the name you prefer to be called?",
    "🎂 When is your birthday?",
    "🎬 What’s your favorite movie genre (action, romance, comedy, etc.)?",
    "📺 Name your top 3 favorite movies or TV shows.",
    "🎨 What’s your favorite color and why?",
    "🍜 What type of cuisine do you like most (Italian, Chinese, desi, etc.)?",
    "👨‍🍳 Do you enjoy cooking? If yes, what’s your go-to dish?",
    "🍉 What’s your favorite fruit and vegetable?",
    "☕ Are you more of a tea or coffee person?",
    "🐶 Do you prefer cats, dogs, or other animals?",
    "🗺️ What’s your dream travel destination?",
    "🏙️ Do you live in a city or a small town?",
    "🍁 What’s your favorite season of the year and why?",
    "🌙 Are you a morning person or a night owl?",
    "📚 Do you like reading books? If yes, what’s the last one you read?",
    "⚽ Do you play any sports or follow any teams?",
    "🎧 What’s your favorite hobby or way to relax?",
    "🎶 What type of music do you enjoy most?",
    "🌄 Are you more of an indoor person or outdoor explorer?"
]

# --- Session state to keep track of current question ---
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
if "previous_answers" not in st.session_state:
    st.session_state.previous_answers = []
if "user_answer" not in st.session_state:
    st.session_state.user_answer = ""

# --- Display current question ---
st.markdown(f"<div class='question-box'><strong>🧊 Your Question:</strong><br>{st.session_state.current_question}</div>", unsafe_allow_html=True)

# --- User answer input ---
st.session_state.user_answer = st.text_area("💬 Your Answer:", value=st.session_state.user_answer, placeholder="Type your awesome response here...")

# --- Next Question logic ---
if st.button("➡️ Next Question"):
    if st.session_state.user_answer.strip():
        st.session_state.previous_answers.append((st.session_state.current_question, st.session_state.user_answer.strip()))
        st.session_state.current_question = random.choice(questions)
        st.session_state.user_answer = ""
    else:
        st.warning("Please answer the question before moving to the next one!")

# --- Display Previous Answers ---
if st.session_state.previous_answers:
    st.markdown("### 📝 Your Past Responses")
    for idx, (q, a) in enumerate(st.session_state.previous_answers[::-1], 1):
        st.markdown(f"<div class='answer-box'><strong>{idx}. {q}</strong><br>{a}</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center;'>💖 Made with black text, pastel love & endless curiosity. Share the link and let the questions flow!</p>", unsafe_allow_html=True)
