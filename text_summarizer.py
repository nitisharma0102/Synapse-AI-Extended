from transformers import AutoTokenizer, AutoModelForSeq2SeqGeneration
import torch

class TextSummarizer:
    def __init__(self, model_name: str = "google/flan-t5-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqGeneration.from_pretrained(model_name)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def chunk_text(self, text: str, max_chunk_size: int = 512) -> list:
        """Split text into smaller chunks for processing"""
        words = text.split()
        chunks = []
        current_chunk = []
        
        for word in words:
            current_chunk.append(word)
            if len(current_chunk) >= max_chunk_size:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
        
        if current_chunk:
            chunks.append(" ".join(current_chunk))
        
        return chunks

    def summarize(self, text: str) -> str:
        """Generate summary using T5 model"""
        try:
            # Split text into chunks
            chunks = self.chunk_text(text)
            summaries = []

            for chunk in chunks:
                # Prepare input
                inputs = self.tokenizer.encode(
                    "summarize: " + chunk,
                    return_tensors="pt",
                    max_length=1024,
                    truncation=True
                ).to(self.device)

                # Generate summary
                summary_ids = self.model.generate(
                    inputs,
                    max_length=150,
                    min_length=40,
                    num_beams=4,
                    no_repeat_ngram_size=2
                )

                summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
                summaries.append(summary)

            # Combine chunk summaries
            final_summary = " ".join(summaries)
            return final_summary

        except Exception as e:
            raise Exception(f"Error generating summary: {str(e)}")