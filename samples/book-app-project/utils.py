from __future__ import annotations

from books import Book


# --- Display Functions (output only) ---


def print_menu() -> None:
    """Display the interactive menu options.

    Used for the interactive menu mode (alternative to CLI arguments).
    """
    print("\n📚 Book Collection App")
    print("1. Add a book")
    print("2. List books")
    print("3. Mark book as read")
    print("4. Remove a book")
    print("5. Exit")


def print_books(books: list[Book]) -> None:
    """Display a list of books in a formatted output with read status."""
    if not books:
        print("No books in your collection.")
        return

    print("\nYour Books:")
    for index, book in enumerate(books, start=1):
        status = "✅ Read" if book.read else "📖 Unread"
        print(f"{index}. {book.title} by {book.author} ({book.year}) - {status}")


def show_help() -> None:
    """Display available CLI commands."""
    print("""
Book Collection Helper

Commands:
  list         - Show all books
  add          - Add a new book
  remove       - Remove a book by title
  find         - Find books by author
  find-title   - Find a book by title
  mark-read    - Mark a book as read
  search-year  - Search books by year range
  help         - Show this help message
""")


def print_error(message: str) -> None:
    """Display an error message in a consistent format."""
    print(f"\nError: {message}\n")


def print_success(message: str) -> None:
    """Display a success message in a consistent format."""
    print(f"\n{message}\n")


# --- Validation Functions (pure logic, no I/O) ---


def validate_non_empty(value: str, field_name: str) -> str | None:
    """Check that a string is non-empty after stripping whitespace.

    Returns:
        An error message string if invalid, or None if valid.
    """
    if not value.strip():
        return f"{field_name} cannot be empty"
    return None


def validate_year_input(year_str: str) -> tuple[int, None] | tuple[None, str]:
    """Parse and validate a year string.

    Returns:
        (year, None) on success, or (None, error_message) on failure.
    """
    if not year_str.strip():
        return None, "Year cannot be empty"
    try:
        year = int(year_str)
    except ValueError:
        return None, f"Invalid year: '{year_str}'. Please enter a number"
    if year < 0:
        return None, "Year cannot be negative"
    return year, None


def validate_menu_choice(choice: str) -> str | None:
    """Validate a menu choice is a digit between 1-5.

    Returns:
        An error message string if invalid, or None if valid.
    """
    if not choice:
        return "Input cannot be empty. Please enter a number between 1 and 5."
    if not choice.isdigit() or not 1 <= int(choice) <= 5:
        return f"Invalid choice: '{choice}'. Please enter a number between 1 and 5."
    return None


# --- Input Functions (combine validation + display) ---


def get_user_choice() -> str:
    """Prompt the user to select a menu option (1-5) with validation.

    Used for the interactive menu mode (alternative to CLI arguments).

    Returns:
        A string representing the user's valid choice ('1' through '5').
    """
    while True:
        choice = input("Choose an option (1-5): ").strip()
        error = validate_menu_choice(choice)
        if error:
            print(error)
            continue
        return choice


def get_book_details() -> tuple[str, str, int]:
    """Interactively prompt the user for book details with input validation.

    Re-prompts until valid input is provided for each field.

    Returns:
        tuple[str, str, int]: A tuple of (title, author, year).
    """
    while True:
        title = input("Enter book title: ").strip()
        error = validate_non_empty(title, "Title")
        if error:
            print(f"{error}. Please enter a title.")
            continue
        break

    while True:
        author = input("Enter author: ").strip()
        error = validate_non_empty(author, "Author")
        if error:
            print(f"{error}. Please enter an author.")
            continue
        break

    while True:
        year_input = input("Enter publication year: ").strip()
        year, error = validate_year_input(year_input)
        if error:
            print(f"{error}. Please enter a valid year.")
            continue
        break

    return title, author, year
