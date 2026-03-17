import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Zen Creator Studio", page_icon="🌿")

# API Key setup from Secrets
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("API Key नहीं मिली! कृपया Secrets चेक करें।")

st.title("🌿 Zen Creator Studio")
st.write(f"नमस्ते VR, शांत मन से अपना टॉपिक बताएं।")

topic = st.text_input("टॉपिक यहाँ लिखें:", placeholder="उदा: MrBeast style challenge")

if st.button("Create My Weekly Magic ✨"):
    if topic:
        with st.spinner("AI सोच रहा है..."):
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(f"Create a viral YouTube script and title for: {topic}")
                st.subheader("आपकी जादुई स्क्रिप्ट:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("कृपया पहले कुछ लिखें!")
