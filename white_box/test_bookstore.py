# -*- coding: utf-8 -*-
"""
Mock up testing examples for BookStore.
"""
import unittest
from unittest.mock import patch

from white_box.book_store import Book, BookStore, main


class TestBook(unittest.TestCase):
    """
    Book unittest class.
    """

    @patch("builtins.print")
    def test_display_book(self, mock_print):
        """
        Test display method shows correct book information.
        """
        # Create a book instance
        book = Book("Python 101", "John Doe", 29.99, 5)

        # Call display method
        book.display()

        # Assert print was called 4 times (title, author, price, quantity)
        self.assertEqual(mock_print.call_count, 4)
        mock_print.assert_any_call("Title: Python 101")
        mock_print.assert_any_call("Author: John Doe")
        mock_print.assert_any_call("Price: $29.99")
        mock_print.assert_any_call("Quantity: 5")


class TestBookStore(unittest.TestCase):
    """
    BookStore unittest class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.bookstore = BookStore()
        self.book1 = Book("Python 101", "John Doe", 29.99, 5)
        self.book2 = Book("Java Basics", "Jane Smith", 39.99, 3)
        self.book3 = Book("C++ Advanced", "Bob Johnson", 49.99, 2)

    @patch("builtins.print")
    def test_add_book_success(self, mock_print):
        """
        Test adding a book to the store.
        """
        # Add book to store
        self.bookstore.add_book(self.book1)

        # Assert book was added
        self.assertEqual(len(self.bookstore.books), 1)
        self.assertEqual(self.bookstore.books[0], self.book1)
        mock_print.assert_called_once_with("Book 'Python 101' added to the store.")

    @patch("builtins.print")
    def test_add_multiple_books(self, mock_print):
        """
        Test adding multiple books to the store.
        """
        # Add multiple books
        self.bookstore.add_book(self.book1)
        self.bookstore.add_book(self.book2)
        self.bookstore.add_book(self.book3)

        # Assert all books were added
        self.assertEqual(len(self.bookstore.books), 3)
        self.assertEqual(mock_print.call_count, 3)

    @patch("builtins.print")
    def test_display_books_empty_store(self, mock_print):
        """
        Test displaying books when store is empty.
        """
        # Display books from empty store
        self.bookstore.display_books()

        # Assert appropriate message is printed
        mock_print.assert_called_once_with("No books in the store.")

    @patch("builtins.print")
    def test_display_books_with_books(self, mock_print):
        """
        Test displaying books when store has books.
        """
        # Add books to store
        self.bookstore.add_book(self.book1)
        self.bookstore.add_book(self.book2)
        mock_print.reset_mock()

        # Display books
        self.bookstore.display_books()

        # Assert header is printed and each book's display is called
        # Header + (4 prints per book * 2 books) = 9 total prints
        self.assertEqual(mock_print.call_count, 9)
        mock_print.assert_any_call("Books available in the store:")

    @patch("builtins.print")
    def test_search_book_found(self, mock_print):
        """
        Test searching for a book that exists in the store.
        """
        # Add book to store
        self.bookstore.add_book(self.book1)
        mock_print.reset_mock()

        # Search for existing book
        self.bookstore.search_book("Python 101")

        # Assert book found message is printed
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(
            any("Found 1 book(s) with title 'Python 101':" in call for call in calls)
        )

    @patch("builtins.print")
    def test_search_book_not_found(self, mock_print):
        """
        Test searching for a book that doesn't exist in the store.
        """
        # Add book to store
        self.bookstore.add_book(self.book1)
        mock_print.reset_mock()

        # Search for non-existing book
        self.bookstore.search_book("Nonexistent Book")

        # Assert not found message is printed
        mock_print.assert_called_once_with(
            "No book found with title 'Nonexistent Book'."
        )

    @patch("builtins.print")
    def test_search_book_case_insensitive(self, mock_print):
        """
        Test that search is case-insensitive.
        """
        # Add book to store
        self.bookstore.add_book(self.book1)
        mock_print.reset_mock()

        # Search with different case
        self.bookstore.search_book("PYTHON 101")

        # Assert book is found
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(
            any("Found 1 book(s) with title 'PYTHON 101':" in call for call in calls)
        )

    @patch("builtins.print")
    def test_search_book_multiple_copies(self, mock_print):
        """
        Test searching when multiple copies of same title exist.
        """
        # Add same book multiple times
        book_copy1 = Book("Python 101", "John Doe", 29.99, 5)
        book_copy2 = Book("Python 101", "Jane Smith", 24.99, 3)

        self.bookstore.add_book(book_copy1)
        self.bookstore.add_book(book_copy2)
        mock_print.reset_mock()

        # Search for book
        self.bookstore.search_book("Python 101")

        # Assert multiple books found
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(
            any("Found 2 book(s) with title 'Python 101':" in call for call in calls)
        )


class TestMain(unittest.TestCase):
    """
    Main function unittest class.
    """

    @patch("builtins.input", side_effect=["1", "4"])
    @patch("builtins.print")
    def test_main_display_books_empty(self, mock_print):
        """
        Test main menu option 1 (display books) with empty store.
        """
        # Run main
        main()

        # Assert display was called and exiting message printed
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(any("No books in the store." in call for call in calls))
        self.assertTrue(any("Exiting..." in call for call in calls))

    @patch(
        "builtins.input",
        side_effect=["3", "Python 101", "John Doe", "29.99", "5", "1", "4"],
    )
    @patch("builtins.print")
    def test_main_add_and_display_book(self, mock_print):
        """
        Test main menu option 3 (add book) and then option 1 (display).
        """
        # Run main
        main()

        # Assert book was added and displayed
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(
            any("Book 'Python 101' added to the store." in call for call in calls)
        )
        self.assertTrue(any("Books available in the store:" in call for call in calls))
        self.assertTrue(any("Title: Python 101" in call for call in calls))

    @patch(
        "builtins.input",
        side_effect=[
            "3",
            "Test Book",
            "Test Author",
            "19.99",
            "10",
            "2",
            "Test Book",
            "4",
        ],
    )
    @patch("builtins.print")
    def test_main_add_and_search_book(self, mock_print):
        """
        Test main menu option 3 (add book) and then option 2 (search).
        """
        # Run main
        main()

        # Assert book was added and found
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(
            any("Book 'Test Book' added to the store." in call for call in calls)
        )
        self.assertTrue(
            any("Found 1 book(s) with title 'Test Book':" in call for call in calls)
        )

    @patch("builtins.input", side_effect=["2", "Nonexistent Book", "4"])
    @patch("builtins.print")
    def test_main_search_not_found(self, mock_print):
        """
        Test main menu option 2 (search) for non-existing book.
        """
        # Run main
        main()

        # Assert not found message printed
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(
            any(
                "No book found with title 'Nonexistent Book'." in call for call in calls
            )
        )

    @patch("builtins.input", side_effect=["5", "4"])
    @patch("builtins.print")
    def test_main_invalid_choice(self, mock_print):
        """
        Test main menu with invalid choice.
        """
        # Run main
        main()

        # Assert invalid choice message printed
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(
            any("Invalid choice. Please try again." in call for call in calls)
        )

    @patch("builtins.input", side_effect=["4"])
    @patch("builtins.print")
    def test_main_exit_immediately(self, mock_print):
        """
        Test main menu with immediate exit (option 4).
        """
        # Run main
        main()

        # Assert exit message printed
        mock_print.assert_any_call("Exiting...")

    @patch(
        "builtins.input",
        side_effect=[
            "3",
            "Book 1",
            "Author 1",
            "10.00",
            "1",
            "3",
            "Book 2",
            "Author 2",
            "20.00",
            "2",
            "1",
            "4",
        ],
    )
    @patch("builtins.print")
    def test_main_add_multiple_books_and_display(self, mock_print):
        """
        Test adding multiple books and displaying them.
        """
        # Run main
        main()

        # Assert both books were added
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(
            any("Book 'Book 1' added to the store." in call for call in calls)
        )
        self.assertTrue(
            any("Book 'Book 2' added to the store." in call for call in calls)
        )
        self.assertTrue(any("Title: Book 1" in call for call in calls))
        self.assertTrue(any("Title: Book 2" in call for call in calls))


if __name__ == "__main__":
    unittest.main()
