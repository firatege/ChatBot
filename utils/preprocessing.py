import pandas as pd
import numpy as np
import re
import nltk
from trnlp import TrnlpWord  # Trnlp kütüphanesi
import colorama as cl
import json
from snowballstemmer import TurkishStemmer

# laod stopwords from json
try:
    with open('../utils/stopWords.json') as f:
        stopwords_tr = json.load(f)
        stopwords_tr = stopwords_tr['stopwords']
except Exception as e:
    print(cl.Fore.RED + f'Stopwords yüklenirken hata: {e}')
    stopwords_tr = []


# TrnlpWord objesi (lemmatizer için)
lemmatizer = TrnlpWord()

def lemmatize_word(word):
    try:
        # Trnlp ile lemmatization işlemi
        lemmatizer.setword(word)
        if lemmatizer.get_base:
            ob = lemmatizer.get_inf[0]
            return ob['verifiedBase']
        else:
            return word  # Eğer lemmatizasyon yapılamazsa, kelimeyi olduğu gibi bırak
    except Exception as e:
        print(cl.Fore.RED + f'Lemmatization hatası: {e}')
        return word  # Hata durumunda kelimeyi olduğu gibi bırak

def preprocess_text(text):
    """
    Metni ön işleme: Küçük harfe çevirme, noktalama işaretlerini kaldırma,
    stopwords temizliği ve kök bulma (lemmatization) işlemleri.
    """
    try:
        # Küçük harfe çevir
        text = text.lower()
        # Sayıları kaldır
        text = re.sub(r'\d+', '', text)
        # Noktalama işaretlerini kaldır
        text = re.sub(r'[^\w\s]', '', text)
        # Fazladan boşlukları kaldır
        text = re.sub(r'\s+', ' ', text)
        # Baş ve sondaki boşlukları temizle
        text = text.strip()

        # Tokenize
        tokens = nltk.word_tokenize(text)
        # Lemmatization
        tokens = [lemmatize_word(word) for word in tokens]
        # Stopwords'i kaldır
        tokens = [word for word in tokens if word not in stopwords_tr]

        # İşlenmiş metni birleştir
        processed_text = ' '.join(tokens)
        return processed_text, tokens
    except Exception as e:
        print(cl.Fore.RED + f'Text preprocessing hatası: {e}')
        return None
