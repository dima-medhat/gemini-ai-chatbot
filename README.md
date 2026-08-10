# 🤖 Gemini AI Chatbot

A stateful conversational AI chatbot built with Python, Streamlit, and the Gemini API.

## 📑 Table of Contents

- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
- [How to Run the Project](#how-to-run-the-project)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Demo Video](#demo-video)

# Project Overview

This project is a Streamlit-based AI chat application that integrates with the Google Gemini model to provide interactive conversations.

The application allows users to start new chats, communicate with the AI, and maintain conversation history throughout the session. Users can revisit previous conversations and continue chatting from where they left off.

It also includes the option for users to enter their own Gemini API key, providing greater flexibility when accessing the AI model.

## Objectives

The main objectives of this project are:

- Learn how to connect a Python application to an LLM API.
- Understand client-server communication when working with AI APIs.
- Build an interactive chatbot interface using Streamlit.
- Manage multiple conversations and chat history.
- Practice stateful AI conversation management.
- Organize Python code using reusable functions.
- Learn how to securely manage API keys using environment variables.

## Features

- Gemini-powered AI responses
- Interactive Streamlit chat interface
- Multiple conversation support
- Conversation history
- Automatic chat title generation
- New chat creation
- Session-based conversation storage
- Secure API key handling

## Technologies Used

| Technology        | Purpose                             |
| ----------------- | ----------------------------------- |
| Python            | Main programming language           |
| Streamlit         | Building the chatbot user interface |
| Google Gemini API | Generating AI responses             |
| Google GenAI SDK  | Connecting Python with Gemini       |
| python-dotenv     | Loading environment variables       |


## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

### 2. Navigate to the project folder

```bash
cd REPOSITORY
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` file

Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

## How to Run the Project

After completing the setup, start the Streamlit application using:

```bash
streamlit run app.py
```

Then open the local URL displayed in the terminal.

Usually:

```text
http://localhost:8501
```

## Project Structure

```text
gemini-chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
│
├── functions/
│   ├── __init__.py
│   ├── llm_service.py
│   └── chat_manager.py
│
├── images/
│   ├── chatbot-home.png
│   ├── conversation-example.png
│
└── README.md
```

### File Description

- `app.py` – Main Streamlit application.
- `llm_service.py` – Handles communication with the Gemini API.
- `chat_manager.py` – Handles conversations and chat history.
- `requirements.txt` – Contains the required Python packages.
- `.env` – Stores private environment variables such as the API key.
- `.gitignore` – Prevents sensitive and unnecessary files from being uploaded to GitHub.
- `images/` – Stores screenshots used in the README.

## Future Improvements

Possible future improvements include:

- Add streaming responses.
- Store conversations permanently using a database.
- Support additional AI models.
- Improve the user interface and customization.
- Add document upload and RAG functionality.
