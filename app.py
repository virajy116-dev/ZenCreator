import streamlit as st
import google.generativeai as genai

# Standard Page Configuration
st.set_page_config(page_title="Zen Creator Studio", page_icon="🌿")

# API Configuration
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("API Key missing in Secrets!")

# Application Title
st.title("Zen Creator Studio")
st.write("Welcome VR. Enter your video topic below.")

# User Input
topic = st.text_input("Enter Topic:", placeholder="e.g. MrBeast style challenge")

# Logic to generate content
if st.button("Generate Script"):
    if topic:
        with st.spinner("AI is processing..."):
            try:
                # Using the latest stable engine
                model = genai.GenerativeModel("gemini-1.5-flash")
                
                # Instruction to AI
                prompt = f"Act as a professional YouTuber. Create a viral script and title in Hinglish for: {topic}"
                
                response = model.generate_content(prompt)
                
                st.divider()
                st.subheader("Your AI Generated Script:")
                st.write(response.text)
            except Exception as e:
                st.error(f"System Error: {str(e)}")
    else:
        st.warning("Please enter a topic first.")
        st.warning("Please enter a topic first!")
        st.warning("कृपया पहले कुछ लिखें!")
