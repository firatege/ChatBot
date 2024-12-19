'''
FASTTEXT TEST
'''

from utils.FastText import FastModel
from utils.preprocessing import preprocess_text
import colorama as cl
import numpy as np

# Sentences
with open('./wiki.tr.txt', 'r', encoding='utf-8') as f:
    #first 1000 lines
    sentences = [next(f) for _ in range(50000)]

# Preprocess the sentences
preprocessed_sentences = [preprocess_text(sentence)[0] for sentence in sentences]
# Initialize the model
# Initialize the model with sentences
model = FastModel(sentences=preprocessed_sentences, vector_size=100, window=5, min_count=1, workers=4, sg=1)
model.train()


# Save the model
model.save('fasttext_model')

