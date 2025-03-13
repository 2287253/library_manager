# Personal Library Manager

A command-line application to manage your personal book collection.

## Features

- Add books to your library with details like title, author, publication year, genre, and read status
- Remove books from your library
- Search for books by title or author
- Display all books in your library
- View statistics about your library (total books, percentage read)
- Automatically save and load your library from a text file

## Requirements

- Python 3.6 or higher

## How to Use

1. Run the program:
   ```
   python library_manager.py
   ```

2. Use the menu to interact with your library:
   - Option 1: Add a book
   - Option 2: Remove a book
   - Option 3: Search for a book
   - Option 4: Display all books
   - Option 5: Display statistics
   - Option 6: Exit

## Data Storage

Your library data is automatically saved to a file named `library.txt` in the same directory as the program. The library is saved:
- Immediately after adding a book
- Immediately after removing a book
- When exiting the program

This ensures your data is always up-to-date and persists between sessions. Each book is stored on a separate line with fields separated by the '|' character.

## Example Usage

```
Welcome to your Personal Library Manager!
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit
Enter your choice: 1

Enter the book title: The Great Gatsby
Enter the author: F. Scott Fitzgerald
Enter the publication year: 1925
Enter the genre: Fiction
Have you read this book? (yes/no): yes
Book added successfully!
Library saved to library.txt.

Welcome to your Personal Library Manager!
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit
Enter your choice: 4

Your Library:
1. The Great Gatsby by F. Scott Fitzgerald (1925) - Fiction - Read

Welcome to your Personal Library Manager!
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit
Enter your choice: 6
Library saved to file. Goodbye! "# library_manager" 
