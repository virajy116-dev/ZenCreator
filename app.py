import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="Zen Creator Studio", page_icon="🌿")

# API Key setup
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except:
    st.error("API Key missing! Please add GEMINI_API_KEY in secrets.")
    st.stop()

# Title
st.title("🌿 Zen Creator Studio")
st.write("Welcome VR. Enter your video topic below.")

# Input
topic = st.text_input("Enter Topic", placeholder="e.g. MrBeast challenge")

# Button
if st.button("Generate Content"):
    if topic.strip() != "":
        with st.spinner("Generating..."):
            try:
                # ✅ Working model
                model = genai.GenerativeModel("gemini-pro")

                prompt = f"""
You are a professional YouTube content creator.

Create in Hinglish:
1. Viral Title
2. Full Script
3. Description
4. 10 Hashtags
5. Viral Caption

Topic: {topic}
"""

                response = model.generate_content(prompt)

                st.divider()
                st.subheader("Your Content")
                st.write(response.text)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a topic first.")
