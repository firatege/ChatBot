# TF-IDF
import numpy as np
import pandas as pd
import utils.preprocessing as pre
import colorama as cl
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# TF-IDF
def calculate_tfidf(query, sentences):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(sentences)
    query_vector = vectorizer.transform([query])
    return vectors, query_vector

# Cosine similarity calculation and result mapping
def calculate_similarity(query_vector, sentence_vectors):
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

    # Calculate TF-IDF
    vectors, query_vector = calculate_tfidf(query, sentences)

    # Calculate similarity
    similarity_scores = calculate_similarity(query_vector, vectors)

    # Display results
    display_results(query, sentences, similarity_scores)

if __name__ == '__main__':
    main()