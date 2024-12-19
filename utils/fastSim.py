import numpy as np
import pandas as pd
import colorama as cl
from sklearn.metrics.pairwise import cosine_similarity
from utils.FastText import FastModel
import utils.preprocessing as pre

class FastTextEntityIntent:
    def __init__(self, model_path, sentences_corpus_size=10000):
        self.model_path = model_path
        self.sentences_corpus_size = sentences_corpus_size
        self.model = self.load_model()

    def load_model(self):
        with open(self.model_path, 'r', encoding='utf-8') as f:
            preprocessed_sentences = [pre.preprocess_text(line)[0] for line in f][:self.sentences_corpus_size]
        model = FastModel(sentences=preprocessed_sentences)
        model.train()
        return model

    def preprocess_and_vectorize(self, sentences):
        preprocessed = [pre.preprocess_text(sentence)[0] for sentence in sentences]
        vectors = []
        valid_sentences = []

        for sentence, preprocessed_sentence in zip(sentences, preprocessed):
            vector = self.model.get_sentence_vector(preprocessed_sentence)
            if vector is not None:
                vector = np.array(vector).reshape(1, -1)  # Normalize vector shape to (1, N)
                vectors.append(vector)
                valid_sentences.append(sentence)

        return vectors, valid_sentences

    def calculate_similarity(self, query_vector, sentence_vectors):
        query_vector = query_vector.reshape(1, -1)  # Ensure query vector shape is (1, N)
        sentence_vectors = [v.reshape(1, -1) for v in sentence_vectors]  # Ensure all sentence vectors are (1, N)
        sentence_vectors = np.vstack(sentence_vectors)  # Stack the vectors
        return cosine_similarity(query_vector, sentence_vectors).reshape(1, -1)

    def display_results(self, query, categories, similarity_scores):
        if len(similarity_scores[0]) != len(categories):
            raise ValueError(
                f"Shape of passed values is {similarity_scores.shape}, indices imply {(1, len(categories))}")

        matrix = pd.DataFrame(similarity_scores, columns=[f'c{i + 1}' for i in range(len(categories))])
        most_similar_idx = matrix.idxmax(axis=1)[0]

        print(f"{cl.Fore.LIGHTBLUE_EX}Query: {query}{cl.Style.RESET_ALL}")
        for idx, category in enumerate(categories):
            score = matrix.iloc[0, idx]
            if most_similar_idx == f'c{idx + 1}':
                print(
                    f"{cl.Fore.LIGHTGREEN_EX}Most similar: {category} with similarity score: {score}{cl.Style.RESET_ALL}")
            else:
                print(f"{cl.Fore.CYAN}Category: {category} with similarity score: {score}{cl.Style.RESET_ALL}")

    def find_entities(self, query, entities):
        query_vector = self.model.get_sentence_vector(pre.preprocess_text(query)[0]).reshape(1, -1)
        entity_vectors, valid_entities = self.preprocess_and_vectorize(entities)
        entity_similarities = self.calculate_similarity(query_vector, entity_vectors)

        print("\n--- Entity Results ---")
        self.display_results(query, valid_entities, entity_similarities)
        max_id = np.argmax(entity_similarities)
        return valid_entities[max_id]

    def find_intents(self, query, intents):
        query_vector = self.model.get_sentence_vector(pre.preprocess_text(query)[0]).reshape(1, -1)
        intent_vectors, valid_intents = self.preprocess_and_vectorize(intents)
        intent_similarities = self.calculate_similarity(query_vector, intent_vectors)

        print("\n--- Intent Results ---")
        self.display_results(query, valid_intents, intent_similarities)
        max_id = np.argmax(intent_similarities)
        return valid_intents[max_id]

# Örnek kullanım:
def main():
    query = "Yarın okul için erken kalkmam gerekiyor mu?"

    # Örnek entities ve intents
    entities = ['Toplantı', 'İş', 'Okul/Ders', 'Spor', 'Eğlence', 'Alışveriş', 'Yemek', 'Uyku', 'Diğer']
    intents = [
        "Kullanıcının aktiviteleri hatırlamasına yardımcı olmak.",
        "Kullanıcının seyahat ve konum bilgilerinde destek sağlamak.",
        "Kullanıcının sağlık ve spor aktivitelerinde destek sağlamak.",
        "Kullanıcının eğitim ve öğrenim süreçlerinde destek sağlamak.",
        "Kullanıcının eğlence ve kültürel aktivitelerinde destek sağlamak.",
        "Kullanıcının alışveriş ve finansal işlemlerinde destek sağlamak.",
        "Kullanıcının beslenme ve diyet süreçlerinde destek sağlamak.",
        "Kullanıcının uyku düzeni ve kalitesinde destek sağlamak.",
        "Kullanıcının diğer aktivitelerinde destek sağlamak."
    ]

    model_path = '../tests/wiki.tr.txt'
    finder = FastTextEntityIntent(model_path=model_path)

    # Entity bulma
    finder.find_entities(query, entities)

    # Intent bulma
    finder.find_intents(query, intents)

if __name__ == "__main__":
    main()