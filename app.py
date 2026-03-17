import streamlit as st
import google.generativeai as genai
import speech_recognition as sr

# 1. AI API Configuration
# अपनी Gemini API Key यहाँ डालें (अगर अभी नहीं है तो इसे ऐसे ही रहने दें)
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-pro')

# 2. Relaxing UI (Zen Style)
st.set_page_config(page_title="Zen Creator AI", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #0F172A; color: #F8FAFC; font-family: 'Poppins', sans-serif; }
    .glass-card { background: rgba(30, 41, 59, 0.7); border-radius: 12px; padding: 25px; border: 1px solid rgba(255, 255, 255, 0.1); margin-top: 20px; box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5); }
    h1 { color: #4ADE80 !important; font-weight: 300; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 Zen Creator Studio")
st.write(f"नमस्ते VR, शांत मन से अपना टॉपिक बताएं।")

# 3. Voice Logic
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("🎤 सुन रहा हूँ... बोलिए")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio, language="hi-IN")
        except:
            return "सुन नहीं पाया, कृपया फिर से बोलें।"

# 4. Interface
col1, col2 = st.columns([1, 4])
with col1:
    if st.button("🎙️"):
        st.session_state.topic = recognize_speech()

with col2:
    topic = st.text_input("टॉपिक यहाँ लिखें या बोलें:", key="topic")

if st.button("Create My Weekly Magic ✨"):
    if topic:
        with st.spinner('7-दिन का जादुई प्लान तैयार हो रहा है...'):
            prompt = f"Topic: {topic}. Create a 7-day YouTube plan with Scripts, Thumbnail ideas, SEO Tags, and Viral Descriptions from Sunday to Saturday. Keep it creative."
            response = model.generate_content(prompt)
            st.markdown(f"<div class='glass-card'>{response.text}</div>", unsafe_allow_html=True)
            st.download_button("💾 Save Plan", response.text, file_name="weekly_plan.txt")
