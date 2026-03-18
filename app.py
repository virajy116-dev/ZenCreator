import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="Zen Creator Studio", page_icon="🌿")

# API Key setup
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("⚠️ API Key missing in Secrets!")
    st.stop()

# Title
st.title("🌿 Zen Creator Studio")
st.write("Welcome VR. Enter your video topic below.")

# Input
topic = st.text_input("Enter Topic:", placeholder="e.g. MrBeast style challenge")

# Button click
if st.button("Generate Content"):
    if topic:
        with st.spinner("AI is generating magic... ✨"):
            try:
                # ✅ Latest working model
                model = genai.GenerativeModel("gemini-1.5-flash-latest")

                # Prompt
                prompt = f"""
You are a professional YouTube content creator.

Create the following in Hinglish:

1. 🔥 Viral Title
2. 🎬 Full YouTube Script
3. 📝 Description
4. #️⃣ Hashtags (10-15)
5. 📢 Viral Caption

Topic: {topic}
"""

                response = model.generate_content(prompt)

                st.divider()

                st.subheader("🚀 Your Content:")
                st.write(response.text)

            except Exception as e:
                st.error(f"❌ System Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter a topic first.")                st.error(f"System Error: {str(e)}")
    else:
        st.warning("Please enter a topic first.")
        st.warning("Please enter a topic first!")
        st.warning("कृपया पहले कुछ लिखें!")
