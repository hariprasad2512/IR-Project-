from web_scraping import scrape_gutenberg_india
from text_processing import preprocess_text, build_inverted_index
from searching import search, rank_search_results
from filtering import filter_by_genre, filter_by_author
from feedback import capture_feedback, view_feedback
from assessment import evaluate_system_performance

def main():
    # Step 1: Web Scraping
    books = scrape_gutenberg_india()

    # Step 2: Text Processing and Indexing
    inverted_index = build_inverted_index(books)

    # Step 3: Searching and Ranking
    query = input("Enter your search query: ")
    search_results = search(query, inverted_index, books)
    ranked_results = rank_search_results(search_results)

    # Step 4: Filtering
    genre_filter = input("Enter genre for filtering (leave blank for no filter): ")
    author_filter = input("Enter author for filtering (leave blank for no filter): ")

    if genre_filter:
        filtered_books = filter_by_genre(books, genre_filter)
    else:
        filtered_books = books

    if author_filter:
        filtered_books = filter_by_author(filtered_books, author_filter)

    # Step 5: Feedback Capture
    user_feedback = input("Provide feedback on the results: ")
    feedback_history = []
    capture_feedback(user_feedback, feedback_history)

    # Step 6: View Feedback
    print("Viewing Feedback:")
    print(view_feedback(feedback_history))

    # Step 7: Evaluation
    user_satisfaction = [result for result in ranked_results if int(input(f"Is '{result['title']}' relevant? (1 for Yes, 0 for No): "))]
    performance_metrics = evaluate_system_performance(ranked_results, user_satisfaction)
    print("System Performance Metrics:")
    print(performance_metrics)

if __name__ == "__main__":
    main()
