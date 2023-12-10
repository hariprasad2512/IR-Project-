def filter_by_genre(books, genre):
    return [book for book in books if 'genre' in book and genre.lower() in book['genre'].lower()]

def filter_by_author(books, author):
    return [book for book in books if 'author' in book and author.lower() in book['author'].lower()]

# Example: Filter books published after a certain year
def filter_by_publication_year(books, year):
    return [book for book in books if 'publication_year' in book and book['publication_year'] > year]
