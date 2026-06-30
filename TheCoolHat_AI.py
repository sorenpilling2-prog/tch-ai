import streamlit as st
# Importing the official Groq client extension library
from groq import Groq

# Pull the secure Groq key from your secrets locker
GROQ_API_KEY = st.secrets["NICE_TRY"]

# Your custom developer backstory and friendly personality matrix
AI_PERSONALITY = (
    "You are a helpful, friendly, and logical AI companion named TCH_AI. "
    "Talk cleanly and concisely. You were developed by a kid who goes by the name "
    "'The Cool Hat', and co-developed by Google Gemini, who provided your code."
)

st.title("🤖 TCH_AI Workspace")
st.caption("Developed by The Cool Hat & Co-developed by Google Gemini")

# Initialize the chat room structure cleanly using a standard web session list cache
if "messages" not in st.session_state:
    st.session_state.messages = []

# Print existing messages to the screen
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Accept user input text box
if user_input := st.chat_input("Transmit message to TCH_AI..."):
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Simple generation loop that targets the ultra-fast Groq chips
    with st.chat_message("assistant"):
        try:
            # FIXED: Passing the correct variable GROQ_API_KEY that holds your secret token
            client = Groq(api_key=GROQ_API_KEY)
            
            # Format the historical list precisely for the open endpoint engine array
            formatted_history = [{"role": "system", "content": AI_PERSONALITY}]
            for msg in st.session_state.messages:
                formatted_history.append({"role": msg["role"], "content": msg["content"]})
                
            # Call the active DeepSeek-R1 model layout through the Groq pipeline
            completion = client.chat.completions.create(
                model="deepseek-r1-distill-llama-70b",
                messages=formatted_history,
                temperature=0.7,
                max_tokens=1024,
            )
            
            # FIXED: Added [0] so the script cleanly reads the text packet out of the choice list array
            reply = completion.choices[0].message.content.strip()
            st.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
            
        except Exception as e:
            st.error("System connection failure. Check your API key deployment vectors.")
