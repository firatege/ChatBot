# TF-IDF
import numpy as np
import pandas as pd
import utils.preprocessing as pre
import utils.FastText as ft
import colorama as cl
from sklearn.metrics.pairwise import cosine_similarity


# Preprocess sentences and get sentence vectors
def preprocess_and_vectorize(sentences, model):
    preprocessed = [pre.preprocess_text(sentence)[0] for sentence in sentences]
    vectors = [model.get_sentence_vector(sentence) for sentence in preprocessed]
    return np.array([v.reshape(1, -1) for v in vectors if v is not None])

# Cosine similarity calculation and result mapping
def calculate_similarity(query_vector, sentence_vectors):
    # Flatten the sentence_vectors array to ensure it is 2D
    sentence_vectors = np.vstack(sentence_vectors)
    return cosine_similarity(query_vector, sentence_vectors).reshape(1, -1)

# Display results

def display_results(query, sentences, similarity_scores):
    matrix = pd.DataFrame(similarity_scores, columns=[f's{i + 1}' for i in range(len(sentences))])
    most_similar_idx = matrix.idxmax(axis=1)[0]

    print(f"{cl.Fore.LIGHTBLUE_EX}Question: {query}{cl.Style.RESET_ALL}")
    for idx, sentence in enumerate(sentences):
        score = matrix.iloc[0, idx]
        if most_similar_idx == f's{idx + 1}':
            print(f"{cl.Fore.LIGHTGREEN_EX}Most similar: {sentence} with similarity score: {score}{cl.Style.RESET_ALL}")
        else:
            print(f"{cl.Fore.CYAN}Sentence: {sentence} with similarity score: {score}{cl.Style.RESET_ALL}")

# Main flow

def main():
    query = 'Berakay Çakıbey Nerede yaşıyor?'
    sentences = [
        'Berakay Çakıbey İstanbul’da yaşıyor.',
        'Berakay Çakıbey Ankara’da yaşıyor.',
        'Berakay Çakıbey İzmir’de yaşıyor.',
        'Berakay Çakıbey Bursa’da yaşıyor.',
        'Berakay Çakıbey Adana’da yaşıyor.',
        'Berakay Çakıbey Yarrağımda’da yaşıyor.',
    ]

    # Load FastText model
    with open('../tests/wiki.tr.txt', 'r', encoding='utf-8') as f:
        preprocessed_sentences = [pre.preprocess_text(next(f))[0] for _ in range(10000)]
        sentences_corpus = [next(f) for _ in range(10000)]
    model = ft.FastModel(sentences=preprocessed_sentences)
    model.train()

    # Process query and sentences
    query_vector = model.get_sentence_vector(pre.preprocess_text(query)[0]).reshape(1, -1)
    sentence_vectors = preprocess_and_vectorize(sentences, model)

    # Calculate similarity
    similarity_scores = calculate_similarity(query_vector, sentence_vectors)

    # Display results
    display_results(query, sentences, similarity_scores)

main()
