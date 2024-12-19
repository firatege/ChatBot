import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.preprocessing import preprocess_text

# Metin temizleme
def preprocess(text):
    """Metni küçük harfe çevirir ve özel karakterleri kaldırır."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]", "", text)
    return text

# TF-IDF matrisi oluşturma
def create_tfidf_matrix(query, database_texts, ngram_range=(1, 2)):
    """Sorgu ve veritabanı metinlerini kullanarak TF-IDF matrisini oluşturur."""
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=ngram_range)
    all_texts = [query] + database_texts
    all_texts = [text for text in all_texts if text]  # Remove empty strings
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    return tfidf_matrix

# Cosine benzerliği hesaplama
def calculate_cosine_similarity(tfidf_matrix, database_size):
    """TF-IDF matrisinden cosine benzerliklerini hesaplar."""
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    entity_similarities = cosine_similarities[0][:database_size]
    intent_similarities = cosine_similarities[0][database_size:]
    return entity_similarities, intent_similarities

# En iyi eşleşmeyi bulma
def find_best_match(similarities, labels):
    """Benzerlik skorlarına göre en iyi eşleşmeyi döner."""
    best_index = similarities.argmax()
    return labels[best_index], similarities[best_index]

# Ana iş akışı
def main():
    # Veritabanından veri alımı
    entities = ['Meeting', 'Market', 'School', 'Sport', 'Work']  # Entity örnekleri
    entity_texts = ['toplantı', 'pazar', 'okul', 'spor', 'iş']  # Entity açıklamaları
    intents = ['Hatırlatıcı','seyehat ve gezi']  # Intent örnekleri
    intent_texts = ['Okuldan sonra spora gidecek miyim?']  # Intent açıklamaları

    # Gelen soru
    query = "Yarın toplantıya gideceğim"  # Örnek soru

    # Temizleme işlemi
    query = preprocess_text(query)
    entity_texts = [preprocess(text) for text in entity_texts]
    intent_texts = [preprocess(text) for text in intent_texts]

    # TF-IDF matrisi oluşturma
    database_texts = entity_texts + intent_texts
    tfidf_matrix = create_tfidf_matrix(query, database_texts)

    # Cosine benzerlikleri hesaplama
    entity_similarities, intent_similarities = calculate_cosine_similarity(tfidf_matrix, len(entity_texts))

    # En iyi entity ve intent eşleşmelerini bulma
    best_entity, entity_score = find_best_match(entity_similarities, entities)
    best_intent, intent_score = find_best_match(intent_similarities, intents)

    # Sonuçları yazdırma
    print(f"En uygun entity: {best_entity} (Benzerlik: {entity_score:.4f})")
    print(f"En uygun intent: {best_intent} (Benzerlik: {intent_score:.4f})")

if __name__ == "__main__":
    main()