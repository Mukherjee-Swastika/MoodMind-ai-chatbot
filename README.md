# 🧠 MoodMind — Emotion-Adaptive AI Chatbot

An AI-powered conversational chatbot that adapts its response style based on the selected personality mode.

MoodMind provides an interactive conversational experience through multiple personality modes, allowing users to communicate with an AI assistant in different emotional styles.

---
## 🚀 Project Overview

Traditional chatbots generally provide responses in a fixed communication style. MoodMind explores a more interactive approach by allowing the user to control the personality and emotional style of the AI assistant.

The system uses different system instructions to dynamically alter the way the AI responds while maintaining the underlying conversational capabilities of the language model.

---
## 🧠 Concepts Explored

This repository provides practical exposure to several Generative AI concepts.

### Large Language Models

Understanding how modern language models generate natural-language responses from user prompts.

### Prompt Engineering

Designing system and user prompts to influence the behavior and output style of an AI model.

### Conversational AI

Building systems capable of maintaining context across multiple user interactions.

### Structured Output

Converting unstructured natural-language information into structured and validated data.

### Text Embeddings

Representing text as numerical vectors for semantic understanding and retrieval.

### Model Integration

Connecting applications with cloud-based and open-source AI models.

### AI Application Development

Converting AI models into usable applications through Streamlit.

---
## 🎯 Project Objectives

 The primary objectives of this project are:

To understand the fundamentals of Generative AI.
To work with Large Language Models.
To explore different LLM providers and open-source models.
To understand prompt engineering.
To build conversational AI applications.
To implement multi-turn conversations.
To experiment with text embeddings.
To implement structured information extraction.
To integrate AI models into interactive applications.
To gain practical experience with modern AI development frameworks.
To understand the process of converting AI models into usable applications.

## 🎯 Main Idea

## ✨ Features

- 🤖 AI-powered conversational interaction
- 🎭 Multiple personality modes
- 🧘 Normal Mode
- 😡 Angry Mode
- 😂 Funny Mode
- 😢 Sad Mode
- 💬 Multi-turn conversations
- 🧠 Context-aware conversation handling
- 🖥️ Interactive Streamlit interface
- 🗑️ Clear conversation functionality
- 🔐 Secure API key management using environment variables

---

## 🎭 Personality Modes

| Mode | Description |
|---|---|
| 🧘 Normal | Helpful, informative and intelligent |
| 😡 Angry | Aggressive and impatient communication style |
| 😂 Funny | Humorous, playful and entertaining |
| 😢 Sad | Emotional and melancholic communication style |

---

## 🛠️ Tech Stack

- **Python**
- **Google Gemini**
- **Google GenAI SDK**
- **Streamlit**
- **LangChain**
- **python-dotenv**

---
# 🔮 Future Enhancements

MoodMind can be further extended into a more advanced AI system.

### 😊 Automatic Emotion Detection

Instead of asking the user to manually select a personality, the system could analyze the user's message and automatically detect the appropriate emotional context.
```text
User Message
     ↓
Emotion Detection Model
     ↓
Detected Emotion
     ↓
Personality Selection
     ↓
Generative AI
     ↓
Adaptive Response


## 📂 Project Structure

```text
MoodMind-ai-chatbot/
│
├── chatmodels/
│   ├── chat.py
│   ├── chatbot.py
│   ├── huggingface.py
│   ├── localmodel.py
│   └── UIchatbot.py
│
├── CineSage/
│   ├── core.py
│   └── UICore.py
│
├── embeddingmodels/
│   ├── embeddings.py
│   └── huggingface_embeddings.py
│
├── .gitignore
├── requirements.txt
└── README.md

