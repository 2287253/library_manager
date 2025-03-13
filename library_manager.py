#!/usr/bin/env python3
"""
Personal Library Manager - A command-line application to manage your book collection.
"""
import os
from datetime import datetime

class LibraryManager:
    """Class to manage a personal library of books."""
    
    def __init__(self):
        """Initialize an empty library and load data if available."""
        self.library = []
        # Use absolute path to ensure file is saved in the correct location
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "library.txt")
        self.load_library()
    
    def add_book(self, title, author, year, genre, read_status):
        """Add a new book to the library."""
        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read_status,
            "date_added": datetime.now().strftime("%Y-%m-%d")
        }
        self.library.append(book)
        # Save library immediately after adding a book
        self.save_library()
        print("Book added successfully!")
    
    def remove_book(self, title):
        """Remove a book from the library by title."""
        initial_count = len(self.library)
        self.library = [book for book in self.library if book["title"].lower() != title.lower()]
        
        if len(self.library) < initial_count:
            # Save library immediately after removing a book
            self.save_library()
            print("Book removed successfully!")
        else:
            print("Book not found in your library.")
    
    def search_by_title(self, title):
        """Search for books by title."""
        matches = [book for book in self.library if title.lower() in book["title"].lower()]
        return matches
    
    def search_by_author(self, author):
        """Search for books by author."""
        matches = [book for book in self.library if author.lower() in book["author"].lower()]
        return matches
    
    def display_books(self, books=None):
        """Display a list of books in a formatted way."""
        if books is None:
            books = self.library
        
        if not books:
            print("No books to display.")
            return
        
        print("\nYour Library:")
        for i, book in enumerate(books, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    
    def display_statistics(self):
        """Display statistics about the library."""
        total_books = len(self.library)
        if total_books == 0:
            print("Your library is empty.")
            return
        
        read_books = sum(1 for book in self.library if book["read"])
        percentage_read = (read_books / total_books) * 100
        
        print(f"\nTotal books: {total_books}")
        print(f"Books read: {read_books}")
        print(f"Percentage read: {percentage_read:.1f}%")
    
    def save_library(self):
        """Save the library to a text file."""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                for book in self.library:
                    read_status = "Read" if book["read"] else "Unread"
                    book_line = f"{book['title']}|{book['author']}|{book['year']}|{book['genre']}|{read_status}|{book['date_added']}\n"
                    file.write(book_line)
            print(f"Library saved to {self.file_path}.")
        except Exception as e:
            print(f"Error saving library: {e}")
            # Print more detailed error information
            import traceback
            traceback.print_exc()
    
    def load_library(self):
        """Load the library from a text file if it exists."""
        if os.path.exists(self.file_path):
            try:
                self.library = []
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        if line.strip():  # Skip empty lines
                            parts = line.strip().split('|')
                            if len(parts) >= 6:
                                title, author, year, genre, read_status, date_added = parts[:6]
                                try:
                                    year_int = int(year)
                                except ValueError:
                                    # Handle case where year is not a valid integer
                                    print(f"Warning: Invalid year '{year}' for book '{title}'. Using 0 instead.")
                                    year_int = 0
                                    
                                book = {
                                    "title": title,
                                    "author": author,
                                    "year": year_int,
                                    "genre": genre,
                                    "read": read_status == "Read",
                                    "date_added": date_added
                                }
                                self.library.append(book)
                print(f"Library loaded from {self.file_path}.")
            except Exception as e:
                print(f"Error loading library: {e}")
                import traceback
                traceback.print_exc()
                self.library = []
        else:
            print(f"No library file found at {self.file_path}. Starting with an empty library.")

def get_menu_choice():
    """Display the menu and get user choice."""
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main function to run the library manager."""
    manager = LibraryManager()
    
    while True:
        choice = get_menu_choice()
        
        if choice == 1:  # Add a book
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            
            while True:
                try:
                    year = int(input("Enter the publication year: "))
                    break
                except ValueError:
                    print("Please enter a valid year.")
            
            genre = input("Enter the genre: ")
            
            while True:
                read_input = input("Have you read this book? (yes/no): ").lower()
                if read_input in ["yes", "y"]:
                    read_status = True
                    break
                elif read_input in ["no", "n"]:
                    read_status = False
                    break
                else:
                    print("Please enter 'yes' or 'no'.")
            
            manager.add_book(title, author, year, genre, read_status)
        
        elif choice == 2:  # Remove a book
            title = input("Enter the title of the book to remove: ")
            manager.remove_book(title)
        
        elif choice == 3:  # Search for a book
            print("\nSearch by:")
            print("1. Title")
            print("2. Author")
            
            while True:
                try:
                    search_choice = int(input("Enter your choice: "))
                    if search_choice in [1, 2]:
                        break
                    else:
                        print("Please enter 1 or 2.")
                except ValueError:
                    print("Please enter a valid number.")
            
            if search_choice == 1:
                query = input("Enter the title: ")
                results = manager.search_by_title(query)
            else:
                query = input("Enter the author: ")
                results = manager.search_by_author(query)
            
            if results:
                print("\nMatching Books:")
                manager.display_books(results)
            else:
                print("No matching books found.")
        
        elif choice == 4:  # Display all books
            manager.display_books()
        
        elif choice == 5:  # Display statistics
            manager.display_statistics()
        
        elif choice == 6:  # Exit
            # Make sure to save the library before exiting
            manager.save_library()
            print("Library saved to file. Goodbye!")
            break

if __name__ == "__main__":
    main() 