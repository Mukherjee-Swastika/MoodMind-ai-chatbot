import streamlit as st

from dotenv import load_dotenv
import os

load_dotenv()

from google import genai


# -------------------- Page Setup --------------------

st.set_page_config(
    page_title="MoodMind Chatbot",
    page_icon="🤖",
    layout="centered"
)


# -------------------- Gemini Setup --------------------

@st.cache_resource
def get_client():

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found in .env file"
        )

    return genai.Client(
        api_key=api_key
    )


client = get_client()


# -------------------- Session State --------------------

if "previous_interaction_id" not in st.session_state:

    st.session_state.previous_interaction_id = None


if "messages" not in st.session_state:

    st.session_state.messages = []


# -------------------- Title --------------------

st.title("🤖 MoodMind Chatbot")

st.write(
    "Emotion-Adaptive AI Chatbot"
)


# -------------------- AI Mode --------------------

st.sidebar.title("🎭 Choose AI Mode")


choice = st.sidebar.selectbox(
    "Select your AI personality",
    [
        "Normal",
        "Angry",
        "Funny",
        "Sad"
    ]
)


if choice == "Normal":

    mode = (
        "You are a helpful and intelligent AI assistant. "
        "Give clear, accurate and useful answers."
    )

elif choice == "Angry":

    mode = (
        "You are an angry AI agent. "
        "You respond aggressively and impatiently, "
        "but you must still be helpful."
    )

elif choice == "Funny":

    mode = (
        "You are a very funny AI agent. "
        "Respond with humor and jokes while remaining helpful."
    )

else:

    mode = (
        "You are a very sad AI agent. "
        "Respond in a sad and emotional tone while remaining helpful."
    )


# -------------------- Clear Chat --------------------

if st.sidebar.button("🗑️ Clear Chat"):

    st.session_state.previous_interaction_id = None

    st.session_state.messages = []

    st.rerun()


# -------------------- Display Chat History --------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# -------------------- Chat Input --------------------

prompt = st.chat_input(
    "Ask MoodMind something..."
)


if prompt:

    # Show user message

    with st.chat_message("user"):

        st.write(prompt)


    # Store user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    # -------------------- Gemini Response --------------------

    with st.chat_message("assistant"):

        with st.spinner("MoodMind is thinking..."):

            try:

                # First message

                if (
                    st.session_state.previous_interaction_id
                    is None
                ):

                    response = client.interactions.create(

                        model="gemini-3.8-flash",

                        input=prompt,

                        system_instruction=mode,

                        generation_config={
                            "thinking_level": "medium"
                        }
                    )


                # Continue conversation

                else:

                    response = client.interactions.create(

                        model="gemini-3.8-flash",

                        input=prompt,

                        previous_interaction_id=(
                            st.session_state.previous_interaction_id
                        ),

                        system_instruction=mode,

                        generation_config={
                            "thinking_level": "medium"
                        }
                    )


                # Get Gemini response

                answer = response.output_text


                # Display response

                st.write(answer)


                # Save interaction ID

                st.session_state.previous_interaction_id = (
                    response.id
                )


                # Save assistant response

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )


            except Exception as e:

                st.error(
                    "MoodMind request failed."
                )

                st.exception(e)