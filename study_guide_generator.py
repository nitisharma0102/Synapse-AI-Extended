from fpdf import FPDF
import re

class StudyGuideGenerator:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def extract_key_concepts(self, text: str) -> list:
        """Extract key concepts from text using simple heuristics"""
        # Split into sentences
        sentences = text.split('. ')
        key_concepts = []
        
        # Simple heuristic: sentences with important keywords
        keywords = ['important', 'key', 'main', 'significant', 'essential']
        for sentence in sentences:
            if any(keyword in sentence.lower() for keyword in keywords):
                key_concepts.append(sentence)
        
        return key_concepts

    def format_content(self, title: str, summary: str) -> dict:
        """Format content into structured sections"""
        key_concepts = self.extract_key_concepts(summary)
        
        # Split summary into bullet points
        points = re.split(r'(?<=[.!?])\s+', summary)
        
        return {
            "title": title,
            "key_concepts": key_concepts,
            "main_points": points
        }

    def generate_pdf(self, content: dict, output_file: str = "study_guide.pdf"):
        """Generate PDF study guide"""
        self.pdf.add_page()
        
        # Title
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(0, 10, content["title"], ln=True, align="C")
        
        # Key Concepts
        self.pdf.set_font("Arial", "B", 12)
        self.pdf.cell(0, 10, "Key Concepts:", ln=True)
        self.pdf.set_font("Arial", "", 12)
        for concept in content["key_concepts"]:
            self.pdf.multi_cell(0, 10, f"• {concept}")
        
        # Main Points
        self.pdf.set_font("Arial", "B", 12)
        self.pdf.cell(0, 10, "Main Points:", ln=True)
        self.pdf.set_font("Arial", "", 12)
        for point in content["main_points"]:
            self.pdf.multi_cell(0, 10, f"• {point}")
        
        self.pdf.output(output_file)