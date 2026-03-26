from __future__ import annotations

import sys
from books import BookCollection
from utils import (
    get_book_details, print_books, print_error, print_success,
    show_help, validate_non_empty,
)


# Global collection instance (initialized in main)
collection: BookCollection | None = None


def handle_list() -> None:
    print_books(collection.list_books())


def handle_add() -> None:
    print("\nAdd a New Book\n")
    title, author, year = get_book_details()

    try:
        collection.add_book(title, author, year)
        print_success("Book added successfully.")
    except (ValueError, OSError) as e:
        print_error(str(e))


def handle_remove() -> None:
    print("\nRemove a Book\n")

    title = input("Enter the title of the book to remove: ").strip()
    error = validate_non_empty(title, "Title")
    if error:
        print_error(error)
        return

    try:
        if collection.remove_book(title):
            print_success("Book removed.")
        else:
            print_error("Book not found.")
    except OSError as e:
        print_error(f"Could not save changes: {e}")


def handle_find() -> None:
    print("\nFind Books by Author\n")

    author = input("Author name: ").strip()
    error = validate_non_empty(author, "Author name")
    if error:
        print_error(error)
        return

    print_books(collection.find_by_author(author))


def handle_mark_read() -> None:
    print("\nMark a Book as Read\n")

    title = input("Enter the title: ").strip()
    error = validate_non_empty(title, "Title")
    if error:
        print_error(error)
        return

    try:
        if collection.mark_as_read(title):
            print_success("Book marked as read.")
        else:
            print_error("Book not found.")
    except OSError as e:
        print_error(f"Could not save changes: {e}")


def handle_find_title() -> None:
    print("\nFind a Book by Title\n")

    title = input("Enter the title: ").strip()
    error = validate_non_empty(title, "Title")
    if error:
        print_error(error)
        return

    book = collection.find_by_title(title)
    if book:
        print_books([book])
    else:
        print_error("Book not found.")


def handle_search_year() -> None:
    print("\nSearch Books by Year Range\n")

    start_str = input("Start year: ").strip()
    end_str = input("End year: ").strip()

    try:
        start = int(start_str)
        end = int(end_str)
        print_books(collection.list_by_year(start, end))
    except ValueError as e:
        print_error(str(e))


def main() -> None:
    global collection
    collection = BookCollection()

    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    commands = {
        "list": handle_list,
        "add": handle_add,
        "remove": handle_remove,
        "find": handle_find,
        "find-title": handle_find_title,
        "mark-read": handle_mark_read,
        "search-year": handle_search_year,
        "help": show_help,
    }

    handler = commands.get(command)
    if handler:
        handler()
    else:
        print("Unknown command.\n")
        show_help()


if __name__ == "__main__":
    main()
