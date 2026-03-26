"""Tests for book_app.py CLI handlers."""

import sys
from unittest.mock import patch
from io import StringIO

import book_app


@patch("book_app.collection")
def test_handle_list_calls_print_books(mock_collection, capsys):
    mock_collection.list_books.return_value = []
    with patch("book_app.print_books") as mock_print:
        book_app.handle_list()
        mock_print.assert_called_once_with([])


@patch("book_app.collection")
@patch("builtins.input", side_effect=["The Hobbit", "Tolkien", "1937"])
def test_handle_add_valid_input(mock_input, mock_collection, capsys):
    book_app.handle_add()
    mock_collection.add_book.assert_called_once_with("The Hobbit", "Tolkien", 1937)
    output = capsys.readouterr().out
    assert "Book added successfully" in output


@patch("builtins.input", side_effect=["Title", "Author", ""])
def test_handle_add_empty_year(mock_input, capsys):
    book_app.handle_add()
    output = capsys.readouterr().out
    assert "Year cannot be empty" in output


@patch("builtins.input", side_effect=["Title", "Author", "abc"])
def test_handle_add_invalid_year(mock_input, capsys):
    book_app.handle_add()
    output = capsys.readouterr().out
    assert "Error" in output


@patch("book_app.collection")
@patch("builtins.input", return_value="The Hobbit")
def test_handle_remove_found(mock_input, mock_collection, capsys):
    mock_collection.remove_book.return_value = True
    book_app.handle_remove()
    output = capsys.readouterr().out
    assert "Book removed" in output


@patch("book_app.collection")
@patch("builtins.input", return_value="Nonexistent")
def test_handle_remove_not_found(mock_input, mock_collection, capsys):
    mock_collection.remove_book.return_value = False
    book_app.handle_remove()
    output = capsys.readouterr().out
    assert "Book not found" in output


@patch("builtins.input", return_value="")
def test_handle_remove_empty_title(mock_input, capsys):
    book_app.handle_remove()
    output = capsys.readouterr().out
    assert "Title cannot be empty" in output


@patch("builtins.input", return_value="")
def test_handle_find_empty_author(mock_input, capsys):
    book_app.handle_find()
    output = capsys.readouterr().out
    assert "Author name cannot be empty" in output


@patch("book_app.collection")
@patch("builtins.input", return_value="Tolkien")
def test_handle_find_valid(mock_input, mock_collection, capsys):
    mock_collection.find_by_author.return_value = []
    with patch("book_app.print_books") as mock_print:
        book_app.handle_find()
        mock_print.assert_called_once()


def test_main_no_args(capsys):
    with patch.object(sys, "argv", ["book_app.py"]):
        book_app.main()
    output = capsys.readouterr().out
    assert "Book Collection Helper" in output


def test_main_unknown_command(capsys):
    with patch.object(sys, "argv", ["book_app.py", "xyz"]):
        book_app.main()
    output = capsys.readouterr().out
    assert "Unknown command" in output


def test_main_routes_to_help(capsys):
    with patch.object(sys, "argv", ["book_app.py", "help"]):
        book_app.main()
    output = capsys.readouterr().out
    assert "Commands:" in output
