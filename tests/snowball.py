import nltk
from snowballstemmer import TurkishStemmer

text = "ama docx formatı kabul etmiyoruz pdf olarak yayınlaman lazım. yayın balığı tutmak isterim"

# Tokenize
words = nltk.word_tokenize(text)

# Küçük harfe çevir ve durdurma kelimelerini kaldır
words = [word.lower() for word in words if word.isalpha()]

# Kelime köklerine indirge (Türkçe için SnowballStemmer)
stemmer = TurkishStemmer()
words = [stemmer.stemWord(word) for word in words]

# Alana özel düzenlemeler (örnek)
print(words)