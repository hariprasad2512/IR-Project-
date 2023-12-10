import time
from flask import Flask, render_template, request

# Import your existing project modules
from web_scraping import scrape_gutenberg_india
from text_processing import preprocess_text, build_inverted_index
from searching import search, rank_search_results
from filtering import filter_by_genre, filter_by_author
from feedback import capture_feedback, view_feedback
from assessment import evaluate_system_performance

app = Flask(__name__)

# Dummy data for demonstration purposes
books = scrape_gutenberg_india()
inverted_index = build_inverted_index(books)

@app.route('/')
def index():
    return render_template('index.html', search_results=None, time_taken=None)

@app.route('/search', methods=['POST'])
def search():
    start_time = time.time()  # Record start time

    query = request.form['query']

    # Implement your search logic here
    words = preprocess_text(query)
    relevant_books = []

    for word in words:
        if word in inverted_index:
            relevant_books.extend(inverted_index[word])

    # Remove duplicates and sort by relevance
    relevant_books = list(set(relevant_books))
    search_results = [{'title': book, 'score': 1.0} for book in relevant_books]
    search_results.sort(key=lambda x: x['score'], reverse=True)

    end_time = time.time()  # Record end time
    time_taken = end_time - start_time

    return render_template('index.html', search_results=search_results, time_taken=time_taken)
