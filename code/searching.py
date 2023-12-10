from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def search(query, inverted_index, books):
    vectorizer = TfidfVectorizer()
    book_texts = [get_book_content(book['url']) for book in books]
    tfidf_matrix = vectorizer.fit_transform(book_texts)
    
    query_vector = vectorizer.transform([preprocess_text(query)])
    cosine_similarities = linear_kernel(query_vector, tfidf_matrix).flatten()
    
    results = [{'title': book['title'], 'score': score} for book, score in zip(books, cosine_similarities)]
    results.sort(key=lambda x: x['score'], reverse=True)
    
    return results

def rank_search_results(results):
    return results
