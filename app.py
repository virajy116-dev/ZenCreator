import streamlit as st
import google.generativeai as genai

# Essential Configuration
st.set_page_config(page_title="AI Video Studio", page_icon="🎥")

# Connect to Gemini API
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("API Key not found in Secrets!")

# App Interface
st.title("🚀 Zen Creator Studio")
st.write("Hello VR! Let's build your next viral video.")

# Input Field
user_topic = st.text_input("Enter your video topic:", placeholder="e.g. MrBeast Challenge")

# Button Logic
if st.button("Generate Script ✨"):
    if user_topic:
        with st.spinner("AI is crafting your script..."):
            try:
                # Using the rock-solid gemini-pro engine
                model = genai.GenerativeModel("gemini-pro")
                
                # The Instruction
                prompt = f"Create a viral YouTube video title and a detailed script in Hinglish for the topic: {user_topic}. Make it high energy and engaging like MrBeast."
                
                response = model.generate_content(prompt)
                
                st.markdown("---")
                st.subheader("🔥 Your Viral Script:")
                st.write(response.text)
                st.success("Success! Copy and start filming.")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a topic first!")
