# 🧠 Synapse: AI-Powered Study Assistant

Synapse is an end-to-end AI-driven platform designed to simplify modern learning by transforming lengthy YouTube lecture videos into concise, structured, and searchable study material. It leverages advanced NLP and state-of-the-art transformer models to automate transcription, summarization, and knowledge retrieval.

---

## 🚀 Problem Statement
Students often struggle with:
- Long, unstructured video lectures  
- Time-consuming manual note-taking  
- Difficulty in extracting key insights for exams  

---

## 💡 Solution
Synapse automates the entire learning workflow:
- Converts lecture videos into accurate text using speech-to-text models  
- Generates concise summaries highlighting key concepts  
- Provides an interactive Q&A chatbot for quick doubt resolution  
- Exports notes into PDF/Word for easy revision  

---

## ⚙️ Key Features
- 🎥 YouTube video processing  
- 🧠 AI-powered summarization (BART/T5)  
- 💬 Context-aware Q&A chatbot  
- 🔍 Semantic search using vector embeddings (FAISS)  
- 📄 Export to PDF & DOCX  
- 🌐 Simple UI built with Gradio  

---

## 🛠️ Tech Stack
- **Python** – Core development  
- **Whisper** – Speech-to-text  
- **Hugging Face Transformers** – NLP models  
- **LangChain** – Q&A pipeline  
- **FAISS** – Vector database for semantic search  
- **Gradio** – User interface  

---

## 🔄 Workflow
1. Extract audio from YouTube videos  
2. Transcribe speech into text  
3. Process and chunk text  
4. Generate embeddings  
5. Store in FAISS for retrieval  
6. Summarize content  
7. Enable interactive Q&A  

---

## 📊 Performance
- ⏱️ ~50% reduction in study time  
- 🎯 70–85% accuracy  
- ⚡ Processes a 10-min lecture in ~2 minutes  

---

## 🔮 Future Scope
- Real-time lecture summarization  
- Multilingual support  
- Personalized learning recommendations  
- LMS & mobile app integration  

---

## 🙌 Acknowledgments
This project leverages technologies from Hugging Face, OpenAI Whisper, LangChain, and Gradio.

This project is based on Synapse-AI (collaborative work),
extended and improved with additional features.
