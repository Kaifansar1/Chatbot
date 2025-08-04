# ---------- STREAMLIT CHAT UI ----------

st.set_page_config(page_title="💬 AI ChatBot", layout="centered")
st.markdown("<h1 style='text-align:center; color:#00A6FB;'>🤖 Real-Time ChatBot </h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Ask me anything: weather, jokes, news, quotes, meanings, general topics!</p>", unsafe_allow_html=True)
st.markdown("---")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("💬 Type your message below:", key="input")

def process_input(user_input):
    if user_input.lower() in ["hi", "hello"]:
        return "👋 Hello! How can I assist you today?"
    elif "weather" in user_input:
        city = user_input.replace("weather", "").strip()
        if not city:
            return "🌍 Please specify a city name."
        return get_weather(city)
    elif "joke" in user_input:
        return get_joke()
    elif "news" in user_input:
        return get_news()
    elif "quote" in user_input:
        return get_quote()
    elif "meaning" in user_input:
        word = user_input.replace("meaning", "").strip()
        if not word:
            return "🔤 Please provide a word."
        return get_meaning(word)
    elif user_input.lower() in ["bye", "exit", "quit"]:
        return "👋 Goodbye! Have a great day!"
    else:
        return get_wiki_summary(user_input)

if user_input:
    response = process_input(user_input)
    st.session_state.chat_history.append(("🧑‍💻 You", user_input))
    st.session_state.chat_history.append(("🤖 Bot", response))

for speaker, text in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {text}")

st.markdown("---")
st.markdown("<p style='text-align:center; font-size:13px; color:gray;'> Developed by Kaif Ansari using Python, RESTful APIs & Streamlit </p>", unsafe_allow_html=True)
