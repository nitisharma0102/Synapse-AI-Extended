from langchain import OpenAI, VectorStore
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain

class StudyGuideBot:
    def __init__(self, api_key: str):
        self.embeddings = HuggingFaceEmbeddings()
        self.text_splitter = CharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        self.llm = OpenAI(openai_api_key=api_key)
        self.vector_store = None
        self.qa_chain = None

    def initialize_knowledge_base(self, text: str):
        """Initialize the bot with study guide content"""
        # Split text into chunks
        texts = self.text_splitter.split_text(text)
        
        # Create vector store
        self.vector_store = FAISS.from_texts(
            texts,
            self.embeddings
        )
        
        # Create QA chain
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            self.llm,
            self.vector_store.as_retriever(),
            return_source_documents=True
        )

    def ask(self, question: str, chat_history: list = None) -> str:
        """Answer questions based on the study guide"""
        if not self.qa_chain:
            raise Exception("Knowledge base not initialized")

        if chat_history is None:
            chat_history = []

        try:
            result = self.qa_chain({"question": question, "chat_history": chat_history})
            return result["answer"]
        except Exception as e:
            raise Exception(f"Error processing question: {str(e)}")