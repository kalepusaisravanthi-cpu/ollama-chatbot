import streamlit as st
import ollama

# Page configuration
st.set_page_config(
    page_title="Ollama Chatbot",
    page_icon="🤖"
)

st.title("🤖 Ollama Chatbot")

# Sidebar
with st.sidebar:
    st.header("Settings")

    model = st.selectbox(
        "Choose a Model",
        ["llama3", "mistral", "phi3"]
    )

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            {
                "role": "system",
                "content": "You are a friendly AI assistant."
            }
        ]
        st.rerun()

# File uploader
uploaded_file = st.file_uploader(
    "Upload a file (Optional)",
    type=["txt", "md", "csv"]
)

file_content = ""

if uploaded_file is not None:
    st.success(f"Uploaded file: {uploaded_file.name}")

    try:
        file_content = uploaded_file.read().decode("utf-8")

        # Limit file size sent to the model
        file_content = file_content[:5000]

    except UnicodeDecodeError:
        st.warning("Unable to read the uploaded file.")
        file_content = ""

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a friendly AI assistant."
        }
    ]

# Display previous messages
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask something...")

if prompt:

    user_prompt = prompt

    # Add uploaded file context
    if file_content:
        user_prompt = f"""
User Question:
{prompt}

Reference Document:
{file_content}
"""

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    # Assistant response
    with st.chat_message("assistant"):

        response_placeholder = st.empty()
        full_response = ""

        try:
            stream = ollama.chat(
                model=model,
                messages=st.session_state.messages,
                stream=True
            )

            for chunk in stream:
                content = chunk["message"]["content"]
                full_response += content

                response_placeholder.markdown(
                    full_response + "▌"
                )

            response_placeholder.markdown(full_response)

            # Save assistant response
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": full_response
                }
            )

        except Exception as e:
            st.error(
                f"Error connecting to Ollama.\n\n"
                f"Make sure Ollama is running and the '{model}' model is installed.\n\n"
                f"Details: {e}"
            )