"""Tests for BookCollection.find_by_author method.

The method should perform case-insensitive substring matching on
the author field, returning all books whose author name contains
the search term.
"""

from __future__ import annotations

import pytest

from books import Book, BookCollection


# ── Fixtures ────────────────────────────────────────────────────


@pytest.fixture()
def collection(tmp_path):
    """Return an empty BookCollection backed by a temp JSON file."""
    return BookCollection(data_file=str(tmp_path / "test_books.json"))


@pytest.fixture()
def orwell_collection(collection):
    """Collection pre-loaded with two George Orwell books."""
    collection.add_book("1984", "George Orwell", 1949)
    collection.add_book("Animal Farm", "George Orwell", 1945)
    return collection


@pytest.fixture()
def multi_author_collection(collection):
    """Collection with books from several authors (some sharing a substring)."""
    collection.add_book("1984", "George Orwell", 1949)
    collection.add_book("Animal Farm", "George Orwell", 1945)
    collection.add_book("Brave New World", "Aldous Huxley", 1932)
    collection.add_book("Curious George", "H. A. Rey", 1941)
    return collection


# ── Happy-path tests ────────────────────────────────────────────


class TestFindByAuthorFullMatch:
    """Searching with the full author name should return matching books."""

    def test_find_by_author_full_name_returns_matching_books(self, orwell_collection):
        # Arrange — fixture already loaded
        # Act
        results = orwell_collection.find_by_author("George Orwell")
        # Assert
        assert len(results) == 2
        assert all(isinstance(b, Book) for b in results)

    def test_find_by_author_full_name_contains_expected_titles(self, orwell_collection):
        results = orwell_collection.find_by_author("George Orwell")
        titles = {b.title for b in results}
        assert titles == {"1984", "Animal Farm"}


# ── Partial-match tests ─────────────────────────────────────────


class TestFindByAuthorPartialMatch:
    """Substring of the author name should still find matching books."""

    def test_find_by_author_partial_last_name_returns_matches(self, orwell_collection):
        results = orwell_collection.find_by_author("Orwell")
        assert len(results) == 2

    def test_find_by_author_partial_first_name_returns_matches(self, orwell_collection):
        results = orwell_collection.find_by_author("George")
        assert len(results) == 2


# ── Case-insensitive tests ──────────────────────────────────────


class TestFindByAuthorCaseInsensitive:
    """Search should be case-insensitive."""

    def test_find_by_author_lowercase_query_matches(self, orwell_collection):
        results = orwell_collection.find_by_author("george orwell")
        assert len(results) == 2

    def test_find_by_author_uppercase_query_matches(self, orwell_collection):
        results = orwell_collection.find_by_author("GEORGE ORWELL")
        assert len(results) == 2

    def test_find_by_author_mixed_case_query_matches(self, orwell_collection):
        results = orwell_collection.find_by_author("gEoRgE oRwElL")
        assert len(results) == 2


# ── Not-found tests ─────────────────────────────────────────────


class TestFindByAuthorNotFound:
    """Non-matching queries should return an empty list."""

    def test_find_by_author_unknown_name_returns_empty(self, orwell_collection):
        results = orwell_collection.find_by_author("Unknown Author")
        assert results == []

    def test_find_by_author_nonexistent_substring_returns_empty(self, orwell_collection):
        results = orwell_collection.find_by_author("Tolkien")
        assert results == []


# ── Multiple authors matching ───────────────────────────────────


class TestFindByAuthorMultipleAuthors:
    """Partial match should return books from different authors when
    the search term is a substring of more than one author name."""

    def test_find_by_author_shared_substring_returns_all_matches(
        self, multi_author_collection
    ):
        # "George" appears in "George Orwell" and in "Curious George" (title, not author)
        # but "George" is a substring of "George Orwell" only among the authors.
        # Let's search for "orwell" — matches only "George Orwell" (2 books)
        results = multi_author_collection.find_by_author("George")
        assert len(results) == 2

    def test_find_by_author_shared_substring_across_authors(self, collection):
        """When multiple authors share a common substring, all should be
        returned."""
        collection.add_book("1984", "George Orwell", 1949)
        collection.add_book("My Struggle", "Karl Ove Knausgård", 2009)
        # Both "George Orwell" and "Karl Ove Knausgård" contain the substring "or"
        # (case-insensitive: "or" in "george orwell" and "or" not in "karl ove knausgård"
        # Actually "or" is not in "Karl Ove Knausgård". Let's pick a better example.)
        # "Ge" is in "George Orwell" only. Let's use a clearer shared substring.
        collection.add_book("The Road", "Cormac McCarthy", 2006)
        # "or" is in "George Orwell" ("or" in "george orwell") ✓
        # "or" is in "Cormac McCarthy" ("or" in "cormac mccarthy") — "cor" has "or" ✓
        results = collection.find_by_author("or")
        authors = {b.author for b in results}
        assert "George Orwell" in authors
        assert "Cormac McCarthy" in authors
        assert len(results) == 2


# ── Empty collection ────────────────────────────────────────────


class TestFindByAuthorEmptyCollection:
    """Searching in an empty collection should return an empty list."""

    def test_find_by_author_empty_collection_returns_empty(self, collection):
        results = collection.find_by_author("George Orwell")
        assert results == []

    def test_find_by_author_empty_collection_returns_list_type(self, collection):
        results = collection.find_by_author("anyone")
        assert isinstance(results, list)
