import streamlit as st
import requests
import wikipedia
from datetime import datetime

# ---------- API-BASED FUNCTIONS ----------

def get_weather(city):
    api_key = "YOUR_WEATHER_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if "main" in data:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"🌡️ Temperature in {city.title()}: {temp}°C, {desc.capitalize()}."
    else:
        return "⚠️ Couldn’t fetch the weather. Please check the city name."

def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.ok:
        joke = response.json()
        return f"😂 {joke['setup']} ... {joke['punchline']}"
    return "😔 Couldn't fetch a joke right now."

def get_news():
    api_key = "YOUR_NEWS_API_KEY"
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    if "articles" in data:
        headlines = [f"📰 {article['title']}" for article in data["articles"][:5]]
        return "\n".join(headlines)
    return "🛑 News not available."

def get_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.ok:
        q = response.json()
        return f"💡 \"{q['content']}\" — *{q['author']}*"
    return "❌ Quote unavailable."

def get_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
        return f"📘 Meaning of **{word}**: {meaning}"
    return "❗ Couldn't find the word."

def get_wiki_summary(query):
    try:
        return "📚 " + wikipedia.summary(query, sentences=2)
    except:
        return "🤷 I couldn't find anything related to that."

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
st.markdown("<p style='text-align:center; font-size:13px; color:gray;'> Developed by Kaif Ansari using Python,RESTful APIs & Streamlit </p>", unsafe_allow_html=True)
