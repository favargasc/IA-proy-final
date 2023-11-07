import spacy
from transformers import pipeline


def sentiments_analyzer(texto: str):
    nlp = spacy.load("en_core_web_sm")

    sentiment_analyzer = pipeline(
        "sentiment-analysis",  model="nlptown/bert-base-multilingual-uncased-sentiment")

    spacy_doc = nlp(texto)

    preprocess = " ".join(token.lemma_ for token in spacy_doc)

    results = sentiment_analyzer(preprocess)
    
    return results
