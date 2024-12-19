from nltk.tokenize import word_tokenize
from utils.preprocessing import preprocess_text
from gensim.models import FastText
import numpy as np
import colorama as cl
import torch


class FastModel:
    # FastText model class
    def __init__(self, sentences, vector_size=100, window=5, min_count=1, workers=4, sg=1):
        self.sentences = sentences  # List of sentences
        self.vector_size = vector_size  # Vector size
        self.window = window  # Window size
        self.min_count = min_count  # Minimum count
        self.workers = workers  # Number of workers
        self.sg = sg  # Skip-gram or CBOW
        self.model = None  # Initialize model as None, to be trained later

    def train(self):
        try:
            self.model = FastText(sentences=self.sentences, vector_size=self.vector_size, window=self.window,
                                  min_count=self.min_count, workers=self.workers, sg=self.sg)  # Train the model
            print(f"{cl.Fore.LIGHTBLUE_EX}Model training successful{cl.Style.RESET_ALL}")
        except Exception as e:
            print(f"{cl.Fore.RED}Error during training: {e}{cl.Style.RESET_ALL}")

    def save(self, file_path):
        if not self.model:
            print(f"{cl.Fore.RED}Model has not been trained yet.{cl.Style.RESET_ALL}")
            return
        try:
            self.model.save(file_path)  # Save the model
            print(f"{cl.Fore.LIGHTBLUE_EX}Model saved successfully at {file_path}{cl.Style.RESET_ALL}")
        except Exception as e:
            print(f"{cl.Fore.RED}Error saving model: {e}{cl.Style.RESET_ALL}")

    def load(self, file_path):
        try:
            self.model = FastText.load(file_path)  # Load the model
            print(f"{cl.Fore.LIGHTBLUE_EX}Model loaded successfully from {file_path}{cl.Style.RESET_ALL}")
        except Exception as e:
            print(f"{cl.Fore.RED}Error loading model: {e}{cl.Style.RESET_ALL}")

    def get_vector(self, word):
        try:
            if word in self.model.wv:
                return self.model.wv[word]  # Get the vector of the word
            else:
                print(f"{cl.Fore.RED}Word '{word}' not found in vocabulary{cl.Style.RESET_ALL}")
                return None
        except Exception as e:
            print(f"{cl.Fore.RED}Error getting vector for word '{word}': {e}{cl.Style.RESET_ALL}")
            return None

    def get_most_similar(self, word, topn=10):  # bigger than 3 later
        try:
            if word in self.model.wv:
                return self.model.wv.most_similar(word, topn=topn)  # Get the most similar words
            else:
                print(f"{cl.Fore.RED}Word '{word}' not found in vocabulary{cl.Style.RESET_ALL}")
                return []
        except Exception as e:
            print(f"{cl.Fore.RED}Error finding most similar words for '{word}': {e}{cl.Style.RESET_ALL}")
            return []

    def get_similarity(self, word1, word2):
        try:
            if word1 in self.model.wv and word2 in self.model.wv:
                return self.model.wv.similarity(word1, word2)  # Get the similarity between two words
            else:
                print(f"{cl.Fore.RED}One or both words '{word1}', '{word2}' not found in vocabulary{cl.Style.RESET_ALL}")
                return None
        except Exception as e:
            print(f"{cl.Fore.RED}Error calculating similarity between '{word1}' and '{word2}': {e}{cl.Style.RESET_ALL}")
            return None

    def get_doesnt_match(self, words):
        try:
            for word in words:
                if word not in self.model.wv:
                    print(f"{cl.Fore.RED}Word '{word}' not found in vocabulary{cl.Style.RESET_ALL}")
                    return None
            return self.model.wv.doesnt_match(words)  # Get the word that doesn't match
        except Exception as e:
            print(f"{cl.Fore.RED}Error finding word that doesn't match in {words}: {e}{cl.Style.RESET_ALL}")
            return None

    def get_word_vector(self, word):
        return self.get_vector(word)

    def get_sentence_vector(self, sentence):
        if self.model is None:
            print(f"{cl.Fore.RED}Model has not been trained or loaded yet.{cl.Style.RESET_ALL}")
            return None
        try:
            tokens = word_tokenize(preprocess_text(sentence)[0])  # Tokenize and preprocess the sentence
            vectors = [self.model.wv[word] for word in tokens if word in self.model.wv]  # Get the vectors of the words

            if not vectors:
                print(f"{cl.Fore.RED}No words in the sentence are in the model's vocabulary{cl.Style.RESET_ALL}")
                return None
            return np.mean(vectors, axis=0)  # Get the mean of the vectors
        except Exception as e:
            print(f"{cl.Fore.RED}Error processing sentence '{sentence}': {e}{cl.Style.RESET_ALL}")
            return None

    def get_sentence_similarity(self, sentence1, sentence2):
        vector1 = self.get_sentence_vector(sentence1)
        vector2 = self.get_sentence_vector(sentence2)

        if vector1 is None or vector2 is None:
            print(f"{cl.Fore.RED}One or both of the sentences could not be processed.{cl.Style.RESET_ALL}")
            return None

        try:
            # Ensure vectors are 1D
            vector1 = np.squeeze(vector1)
            vector2 = np.squeeze(vector2)

            # Calculate cosine similarity
            similarity = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
            return similarity
        except Exception as e:
            print(f"{cl.Fore.RED}Error calculating similarity: {e}{cl.Style.RESET_ALL}")
            return None


    def get_two_words_similarity(self, word1, word2):
        try:
            if word1 in self.model.wv and word2 in self.model.wv:
                return self.model.wv.similarity(word1, word2)  # Get the similarity between two words
            else:
                print(f"{cl.Fore.RED}One or both words '{word1}', '{word2}' not found in vocabulary{cl.Style.RESET_ALL}")
                return None
        except Exception as e:
            print(f"{cl.Fore.RED}Error calculating similarity between '{word1}' and '{word2}': {e}{cl.Style.RESET_ALL}")
            return None