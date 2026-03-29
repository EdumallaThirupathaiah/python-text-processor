positive_words = ["good", "happy", "great", "excellent", "love"]
negative_words = ["bad", "sad", "worst", "hate", "angry"]

def score_text(text):
    score = 0
    for word in text.split():
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1
    return score

def score_chunks(chunks):
    return [(chunk, score_text(chunk)) for chunk in chunks]
