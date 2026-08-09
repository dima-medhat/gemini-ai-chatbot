import streamlit as st
from google import genai

from functions.llm_service import (
    generate_chat_title,
    generate_response,
)

from functions.chat_manager import (
    add_message,
    create_new_chat,
    update_chat_title,
)


# Page settings
st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖",
    layout="wide",
)

st.title("Gemini Chatbot")
st.markdown("🚀 A Streamlit Chatbot Powered By Gemini AI")


# Store API key in session
if "api_key" not in st.session_state:
    st.session_state.api_key = None


# Store all conversations
if "conversations" not in st.session_state:
    st.session_state.conversations = {}


# Create the first chat
if "active_chat_id" not in st.session_state:
    st.session_state.active_chat_id = create_new_chat(
        st.session_state.conversations
    )


# Sidebar
with st.sidebar:
    st.title("Gemini AI ChatBot 🤖")

    st.link_button(
        label="Click here to get API KEY",
        url="https://aistudio.google.com",
        use_container_width=True,
    )

    user_api_key = st.text_input(
        "Gemini API_KEY",
        type="password",
    )

    st.markdown(
        "Your API key is used only for this session "
        "and is not saved permanently."
    )

    submit_button = st.button("Enter")

    # Save user API key
    if submit_button:
        if user_api_key:
            st.session_state.api_key = user_api_key
            st.success("API Key added successfully.")
        else:
            st.error("Please enter your Gemini API key.")

    # Create new chat
    if st.button("➕ New Chat", use_container_width=True):
        new_chat_id = create_new_chat(
            st.session_state.conversations
        )

        st.session_state.active_chat_id = new_chat_id
        st.rerun()

    st.divider()
    st.subheader("Chat History")

    # Show saved chats
    for chat_id, chat_data in st.session_state.conversations.items():

        if st.button(
            chat_data["title"],
            key=f"chat_{chat_id}",
            use_container_width=True,
        ):
            st.session_state.active_chat_id = chat_id
            st.rerun()


# Create Gemini client from user's API key
client = None

if st.session_state.api_key:
    client = genai.Client(
        api_key=st.session_state.api_key
    )


# Get selected chat
active_chat = st.session_state.conversations[
    st.session_state.active_chat_id
]


# Display old messages
for message in active_chat["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User input
prompt = st.chat_input("Ask Gemini anything...")


if prompt:

    # Make sure API key exists
    if client is None:
        st.warning(
            "Please enter your Gemini API key in the sidebar first."
        )
        st.stop()

    # Save user message
    add_message(
        st.session_state.conversations,
        st.session_state.active_chat_id,
        "user",
        prompt,
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate title only for first message
    if len(active_chat["messages"]) == 1:
        try:
            title = generate_chat_title(
                prompt,
                client,
            )

            update_chat_title(
                st.session_state.conversations,
                st.session_state.active_chat_id,
                title,
            )

        except Exception as error:
            print(f"Title generation error: {error}")

    try:
        # Generate AI response
        with st.spinner("Thinking..."):
            response = generate_response(
                active_chat["messages"],
                client,
            )

        # Save assistant message
        add_message(
            st.session_state.conversations,
            st.session_state.active_chat_id,
            "assistant",
            response,
        )

        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(response)

        # Refresh sidebar title
        st.rerun()

    except Exception as error:
        st.error(
            f"{type(error).__name__}: {error}"
        )