# 🤖 Conversational AI Application using LangChain & Groq API

A conversational AI chatbot built using **Python**, **LangChain**, and the **Groq API**. This project demonstrates the fundamentals of integrating Large Language Models (LLMs) into a Python application, managing conversation history, and building interactive AI assistants.

## 🚀 Features

- 💬 Interactive command-line chatbot
- 🧠 Powered by Groq LLMs through LangChain
- 📜 Maintains conversation history during the session
- 🔑 Secure API key management using `.env`
- 🛠️ Clean and beginner-friendly code structure

## 🛠️ Tech Stack

- Python
- LangChain
- Groq API
- python-dotenv

## 📂 Project Structure

```
Simple_chatbot/
│
├── chatbot.py          # Main chatbot application
├── .env_sample         # Sample of .env file 
├── requirements.txt    # Project dependencies
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/PriyanshuSingh44/Simple_chatbot.git
cd Simple_chatbot
```

### 2. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a file named `.env` in the project directory.

```env
GROQ_API_KEY=your_api_key_here
model_name=your_model_name_of_choice
```

## ▶️ Run the Project

```bash
python app.py
```

Start chatting with the AI directly from your terminal.

## 📚 What I Learned

Through this project, I learned how to:

- Integrate LLMs using LangChain
- Connect to the Groq API
- Manage API keys securely with `.env`
- Build conversational AI applications
- Maintain chat history within a session

## 👤 Author

**Priyanshu Singh**

- GitHub: https://github.com/PriyanshuSingh44
- LinkedIn: https://linkedin.com/in/priyanshu-singh-ai
