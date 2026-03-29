from concurrent.futures import ProcessPoolExecutor
import re

def clean_text(text):
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text.lower()

class TextLoader:
    def process(self, text):
        chunks = text.split(".")
        with ProcessPoolExecutor() as executor:
            cleaned = list(executor.map(clean_text, chunks))
        return cleaned
