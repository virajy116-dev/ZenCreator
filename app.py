import streamlit as st
import google.generativeai as genai

# Setup Page
st.set_page_config(page_title="Zen Creator Studio", page_icon="🌿")

# Initialize API
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Key not found in Secrets!")

# User Interface
st.title("🌿 Zen Creator Studio")
st.write("Namaste VR, enter your topic below:")

# Input area
topic = st.text_input("Topic:", placeholder="e.g. MrBeast style challenge")

if st.button("Create Magic ✨"):
    if topic:
        with st.spinner("AI is thinking..."):
            try:
                # Using the latest stable model
                model = genai.GenerativeModel("gemini-1.5-flash")
                
                # Command to AI
                prompt = f"Write a viral YouTube script and title in Hinglish for: {topic}"
                response = model.generate_content(prompt)
                
                st.markdown("---")
                st.subheader("🚀 Your Script:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a topic first!")
        st.warning("कृपया पहले कुछ लिखें!")
