'''
 This file is used to test the preprocessing.py file.
'''

import utils.preprocessing as preprocessing


# tokenizer, tagger, parser and vectorizer

sentence = 'ama docx formatı kabul etmiyoruz pdf olarak yayınlaman lazım. yayın balığı tutmak isterim'


pre,token = preprocessing.preprocess_text(sentence)

print(f'Original sentence: {sentence} \nPreprocessed sentence: {pre} \nTokens: {token}')


# lemmatizer

word = 'isterim'
import trnlp
lemmatizer = trnlp.TrnlpWord()
lemmatizer.setword(word)
print(lemmatizer.get_inf[0])
