"""Tests for get_book_details() in utils.py."""

from __future__ import annotations

from unittest.mock import patch

import pytest

from utils import get_book_details


class TestGetBookDetailsValid:
    """Tests where all inputs are valid on the first attempt."""

    @patch("builtins.input", side_effect=["Python Basics", "John Doe", "2020"])
    def test_valid_input(self, mock_input):
        result = get_book_details()
        assert result == ("Python Basics", "John Doe", 2020)

    @patch("builtins.input", side_effect=["A" * 1000, "Author", "2000"])
    def test_very_long_title(self, mock_input):
        title, author, year = get_book_details()
        assert title == "A" * 1000
        assert author == "Author"
        assert year == 2000

    @patch("builtins.input", side_effect=["Test", "Jean-Paul Sartre", "1943"])
    def test_special_characters_hyphen(self, mock_input):
        assert get_book_details() == ("Test", "Jean-Paul Sartre", 1943)

    @patch("builtins.input", side_effect=["Test", "García Márquez", "1967"])
    def test_special_characters_accents(self, mock_input):
        assert get_book_details() == ("Test", "García Márquez", 1967)

    @patch("builtins.input", side_effect=["Test", "O'Brien", "2010"])
    def test_special_characters_apostrophe(self, mock_input):
        assert get_book_details() == ("Test", "O'Brien", 2010)

    @patch("builtins.input", side_effect=["吾輩は猫である", "夏目漱石", "1905"])
    def test_unicode_japanese(self, mock_input):
        assert get_book_details() == ("吾輩は猫である", "夏目漱石", 1905)

    @patch("builtins.input", side_effect=["📚 Book of Emoji 🎉", "Author", "2023"])
    def test_unicode_emoji(self, mock_input):
        assert get_book_details() == ("📚 Book of Emoji 🎉", "Author", 2023)

    @patch("builtins.input", side_effect=["Title", "Author", "0"])
    def test_year_zero(self, mock_input):
        assert get_book_details() == ("Title", "Author", 0)


class TestGetBookDetailsRetry:
    """Tests where invalid input triggers re-prompts before valid input."""

    @patch("builtins.input", side_effect=["", "Valid Title", "Author", "2020"])
    def test_empty_title_then_valid(self, mock_input):
        result = get_book_details()
        assert result == ("Valid Title", "Author", 2020)
        assert mock_input.call_count == 4

    @patch("builtins.input", side_effect=["Title", "", "Valid Author", "2020"])
    def test_empty_author_then_valid(self, mock_input):
        result = get_book_details()
        assert result == ("Title", "Valid Author", 2020)
        assert mock_input.call_count == 4

    @patch("builtins.input", side_effect=["Title", "Author", "", "2020"])
    def test_empty_year_then_valid(self, mock_input):
        result = get_book_details()
        assert result == ("Title", "Author", 2020)
        assert mock_input.call_count == 4

    @patch("builtins.input", side_effect=["Title", "Author", "abc", "2020"])
    def test_invalid_year_format_then_valid(self, mock_input):
        result = get_book_details()
        assert result == ("Title", "Author", 2020)
        assert mock_input.call_count == 4

    @patch("builtins.input", side_effect=["Title", "Author", "-5", "1990"])
    def test_negative_year_then_valid(self, mock_input):
        result = get_book_details()
        assert result == ("Title", "Author", 1990)
        assert mock_input.call_count == 4

    @patch("builtins.input", side_effect=["   ", "Valid Title", "Author", "2020"])
    def test_whitespace_only_title_rejected(self, mock_input):
        result = get_book_details()
        assert result == ("Valid Title", "Author", 2020)
        assert mock_input.call_count == 4

    @patch(
        "builtins.input",
        side_effect=[
            "",        # empty title
            "   ",     # whitespace title
            "Title",   # valid title
            "",        # empty author
            "Author",  # valid author
            "abc",     # non-numeric year
            "-1",      # negative year
            "",        # empty year
            "2020",    # valid year
        ],
    )
    def test_multiple_invalid_attempts_then_valid(self, mock_input):
        result = get_book_details()
        assert result == ("Title", "Author", 2020)
        assert mock_input.call_count == 9
