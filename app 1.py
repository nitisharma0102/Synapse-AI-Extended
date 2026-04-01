import streamlit as st
from audio_extractor import AudioExtractor
from text_summarizer import TextSummarizer
from study_guide_generator import StudyGuideGenerator
from chatbot import StudyGuideBot
import os

# Initialize components
@st.cache_resource
def initialize_components():
    return {
        "audio_extractor": AudioExtractor(),
        "summarizer": TextSummarizer(),
        "guide_generator": StudyGuideGenerator(),
        "chatbot": StudyGuideBot(st.secrets["OPENAI_API_KEY"])
    }

def main():
    st.title("Synapse - AI Study Assistant")
    
    # Initialize components
    components = initialize_components()
    
    # YouTube URL input
    youtube_url = st.text_input("Enter YouTube Video URL:")
    
    if youtube_url:
        with st.spinner("Processing video..."):
            # Extract and transcribe audio
            transcript = components["audio_extractor"].process_video(youtube_url)
            st.success("Audio extracted and transcribed!")
            
            # Generate summary
            summary = components["summarizer"].summarize(transcript)
            st.success("Summary generated!")
            
            # Create study guide
            content = components["guide_generator"].format_content(
                "Study Guide",
                summary
            )
            components["guide_generator"].generate_pdf(content)
            
            # Initialize chatbot
            components["chatbot"].initialize_knowledge_base(summary)
            
            # Display summary and enable download
            st.subheader("Study Guide")
            st.write(summary)
            
            with open("study_guide.pdf", "rb") as file:
                st.download_button(
                    "Download PDF Study Guide",
                    file,
                    "study_guide.pdf"
                )
    
    # Chat interface
    st.subheader("Ask Questions")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask about the content..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            response = components["chatbot"].ask(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()