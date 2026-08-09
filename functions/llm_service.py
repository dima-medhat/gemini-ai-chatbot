
from google.genai import types


# Gemini model
MODEL_NAME = "gemini-3.5-flash-lite"


def convert_messages_for_gemini(messages: list) -> list:
    gemini_messages = []

    # Convert our chat format to Gemini format
    for message in messages:
        role = message["role"]
        content = message["content"]

        # Skip empty messages
        if not content:
            continue

        # Gemini uses "model" instead of "assistant"
        if role == "assistant":
            role = "model"
        elif role != "user":
            continue

        gemini_messages.append(
            types.Content(
                role=role,
                parts=[
                    types.Part.from_text(
                        text=content
                    )
                ],
            )
        )

    return gemini_messages


def generate_response(
    messages: list[dict],
    client,
) -> str:

    if not messages:
        raise ValueError(
            "Conversation history is empty."
        )

    # Convert conversation history
    gemini_messages = convert_messages_for_gemini(
        messages
    )

    # Stream Gemini response
    stream = client.models.generate_content_stream(
        model=MODEL_NAME,
        contents=gemini_messages,
    )

    full_response = ""

    # Combine all chunks
    for chunk in stream:
        if chunk.text:
            full_response += chunk.text

    if not full_response:
        raise ValueError(
            "Gemini did not return a response."
        )

    return full_response.strip()


def generate_chat_title(
    user_prompt: str,
    client,
) -> str:

    title_prompt = f"""
Generate a short title for this conversation.

Rules:
- Maximum 5 words
- Return only the title
- Do not use quotation marks
- Do not end with a period
- Describe the main topic

User message:
{user_prompt}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=title_prompt,
    )

    if not response.text:
        return "New Chat"

    return response.text.strip()
        