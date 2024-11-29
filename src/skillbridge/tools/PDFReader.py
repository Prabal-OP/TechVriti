from crewai.tools import tool
from PyPDF2 import PdfReader

class PDFReader:
    @tool('PDFReader')
    def read_pdf(file_path:str)  -> str:
        """
        Reads a PDF file and returns its text content.

        Args:
            file_path (str): Path to the PDF file to be read.

        Returns:
            str: Extracted text from the PDF.
        """
        try:
            # Initialize the PDF reader
            reader = PdfReader(file_path)
            content = []
            # Iterate over all pages and extract text
            for page in reader.pages:
                content.append(page.extract_text())
            # Join the text from all pages into a single string
            return "\n".join(content)
        except Exception as e:
            return f"An error occurred while reading the PDF: {str(e)}"