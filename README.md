# ollama-chatbot
# 🤖 Ollama Chatbot using Streamlit

A simple and interactive AI chatbot built using **Streamlit** and **Ollama** that allows users to chat with locally running Large Language Models (LLMs). The application supports real-time streaming responses, chat history, multiple model selection, and optional file uploads for context-aware conversations.

## ✨ Features

* 💬 Interactive chat interface using Streamlit
* 🧠 Integration with Ollama for running local LLMs
* ⚡ Real-time streaming responses
* 📂 Optional file upload support (`.txt`, `.md`, `.csv`)
* 📝 Uses uploaded file content as additional context
* 🔄 Persistent chat history during the session
* 🗑️ Clear chat functionality
* 🤖 Support for multiple Ollama models (Llama 3, Mistral, Phi-3)
* ⚠️ Error handling for unavailable models or Ollama service issues

## 📸 Application Overview

This project demonstrates how to build a lightweight AI assistant that runs entirely on your local machine without relying on external APIs. Since Ollama executes models locally, users maintain control over their data and can experiment with different open-source language models.

## 🛠️ Technologies Used

* Python
* Streamlit
* Ollama
* Large Language Models (LLMs)

## 📋 Prerequisites

Before running this application, ensure the following are installed:

1. Python 3.9 or higher
2. Ollama installed on your system

### Install Ollama

Download and install Ollama from:

https://ollama.com/download

Verify the installation:

```bash
ollama --version
```

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/ollama-chatbot.git
cd ollama-chatbot
```

### Step 2: Create a Virtual Environment (Recommended)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Alternatively:

```bash
pip install streamlit ollama
```

## 🚀 Download an Ollama Model

Before running the chatbot, download at least one supported model.

Example:

```bash
ollama pull llama3
```

Other supported models:

```bash
ollama pull mistral
ollama pull phi3
```

## ▶️ Running the Application

### Start Ollama

```bash
ollama serve
```

### Launch the Streamlit App

```bash
streamlit run app.py
```

After running the command, open the local URL displayed in the terminal (usually `http://localhost:8501`).

## 📁 Project Structure

```text
ollama-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
    └── chatbot_demo.png
```

## 🧠 About Ollama

Ollama is a platform that allows developers to run open-source Large Language Models directly on their local machines. Unlike cloud-based AI services, Ollama provides:

* Improved privacy since data remains on your device
* Offline capabilities after models are downloaded
* Support for multiple open-source models
* Easy integration with Python applications

Learn more: https://ollama.com/

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

* Building AI-powered applications using Streamlit
* Integrating local LLMs into Python applications
* Managing session state in Streamlit
* Implementing streaming responses
* Handling user-uploaded files for contextual AI interactions
* Designing user-friendly interfaces for AI applications

## 🔮 Future Enhancements

* Support for PDF and DOCX files
* Export chat history functionality
* Voice input and speech synthesis
* User authentication
* Conversation persistence using a database
* Support for additional Ollama models

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

## 📄 License

This project is open source and available under the MIT License.

---


