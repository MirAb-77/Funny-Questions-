import streamlit as st
import random

# Set page config for mobile-friendliness and emoji icon
st.set_page_config(page_title="Icebreaker Quest 🎲", page_icon="❄️", layout="centered")

# Inject custom CSS for aesthetic design
st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #FAF3F0;
            color: black;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextArea textarea {
            background-color: #FFF8E7;
            color: black;
            border: 1px solid #D8BFD8;
        }
        .question-box {
            background-color: #E6E6FA;
            padding: 20px;
            border-radius: 15px;
            border: 2px dashed #B39DDB;
            margin-top: 20px;
        }
        .answer-box {
            background-color: #FFE4E1;
            padding: 15px;
            border-radius: 12px;
            border: 1px solid #D8BFD8;
            margin-top: 15px;
            box-shadow: 1px 1px 8px #D8BFD8;
        }
        .center {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='center'>🎀 Icebreaker Quest 🎀</h1>", unsafe_allow_html=True)
st.markdown("<p class='center'>A pastel party of fun questions to spark joy and connections ✨</p>", unsafe_allow_html=True)

# Icebreaker questions
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

# Button to get a new question
if st.button("✨ Reveal My Icebreaker Question ✨"):
    q = random.choice(questions)
    st.markdown(f"<div class='question-box'><strong>🧊 Your Question:</strong><br>{q}</div>", unsafe_allow_html=True)

    # Input area
    user_answer = st.text_area("💬 Your Answer:", placeholder="Type your magical thoughts here...")

    if user_answer:
        st.markdown(f"<div class='answer-box'><strong>💡 Your Response:</strong><br>{user_answer}</div>", unsafe_allow_html=True)
        st.balloons()

else:
    st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", use_column_width=True)
    st.info("Click the button to begin your pastel adventure 💜")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Built with ❤️ and lavender vibes. Share the link to melt the ice with anyone!</p>", unsafe_allow_html=True)
