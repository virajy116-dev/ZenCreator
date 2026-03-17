import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Zen Creator Studio", page_icon="🌿")

# API Key setup from Secrets
try:
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
    else:
        st.error("API Key नहीं मिली! कृपया Manage app > Settings > Secrets में GEMINI_API_KEY डालें।")
except Exception as e:
    st.error(f"Secrets Error: {e}")

# UI Design
st.title("🌿 Zen Creator Studio")
st.write(f"नमस्ते VR, शांत मन से अपना टॉपिक बताएं।")

topic = st.text_input("टॉपिक यहाँ लिखें:", placeholder="उदा: MrBeast style challenge")

if st.button("Create My Weekly Magic ✨"):
    if topic:
        with st.spinner("AI सोच रहा है..."):
            try:
                # Using the stable 'gemini-pro' model
                model = genai.GenerativeModel("gemini-pro")
                response = model.generate_content(f"Create a viral YouTube script and title for: {topic}")
                
                st.markdown("---")
                st.subheader("🚀 आपकी जादुई स्क्रिप्ट:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("कृपया पहले कुछ लिखें!")
