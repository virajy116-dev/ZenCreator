import streamlit as st
from openai import OpenAI

# Page setup
st.set_page_config(page_title="Zen Creator Studio", page_icon="🌿")

# API Key
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    st.error("API Key missing! Add it in Streamlit secrets.")
    st.stop()

# UI
st.title("🌿 Zen Creator Studio")
st.write("Welcome VR. Enter your video topic below.")

topic = st.text_input("Enter Topic", placeholder="e.g. MrBeast challenge")

if st.button("Generate Content"):
    if topic.strip() != "":
        with st.spinner("Generating..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {"role": "system", "content": "You are a professional YouTube content creator."},
                        {"role": "user", "content": f"""
Create in Hinglish:
1. Viral Title
2. Full Script
3. Description
4. 10 Hashtags
5. Viral Caption

Topic: {topic}
"""}
                    ]
                )

                st.divider()
                st.subheader("Your Content")
                st.write(response.choices[0].message.content)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a topic first.")
