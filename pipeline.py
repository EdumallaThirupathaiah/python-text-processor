from module.loader import TextLoader
from module.scorer import score_chunks
from module.storage import insert_data

def run_pipeline(text):
    loader = TextLoader()
    cleaned_chunks = loader.process(text)

    scored = score_chunks(cleaned_chunks)

    for chunk, score in scored:
        insert_data(text, chunk, score)

    return scored
