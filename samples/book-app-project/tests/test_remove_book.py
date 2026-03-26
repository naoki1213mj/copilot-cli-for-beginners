"""Tests for BookCollection.remove_book method."""

import pytest

from books import Book, BookCollection, BookNotFoundError, BookValidationError


@pytest.fixture()
def collection(tmp_path):
    return BookCollection(data_file=str(tmp_path / "test_books.json"))


class TestRemoveBookSuccess:
    """Happy-path scenarios for remove_book."""

    def test_remove_existing_book_removes_from_list(self, collection):
        collection.add_book("Dune", "Frank Herbert", 1965)

        collection.remove_book("Dune")

        assert all(b.title != "Dune" for b in collection.list_books())

    def test_remove_book_case_insensitive_lowercase(self, collection):
        collection.add_book("Dune", "Frank Herbert", 1965)

        collection.remove_book("dune")

        assert collection.list_books() == []

    def test_remove_book_case_insensitive_uppercase(self, collection):
        collection.add_book("Dune", "Frank Herbert", 1965)

        collection.remove_book("DUNE")

        assert collection.list_books() == []

    def test_remove_book_whitespace_padded_title(self, collection):
        collection.add_book("Dune", "Frank Herbert", 1965)

        collection.remove_book("  Dune  ")

        assert collection.list_books() == []

    def test_remove_book_returns_true(self, collection):
        collection.add_book("Dune", "Frank Herbert", 1965)

        result = collection.remove_book("Dune")

        assert result is True

    def test_remove_book_persists_to_disk(self, collection, tmp_path):
        collection.add_book("Dune", "Frank Herbert", 1965)
        collection.add_book("1984", "George Orwell", 1949)

        collection.remove_book("Dune")

        reloaded = BookCollection(data_file=str(tmp_path / "test_books.json"))
        titles = [b.title for b in reloaded.list_books()]
        assert "Dune" not in titles
        assert "1984" in titles


class TestRemoveBookErrors:
    """Error scenarios for remove_book."""

    def test_remove_book_not_found_raises(self, collection):
        with pytest.raises(BookNotFoundError, match="Nonexistent"):
            collection.remove_book("Nonexistent")

    def test_remove_book_empty_collection_raises(self, collection):
        with pytest.raises(BookNotFoundError):
            collection.remove_book("Dune")

    def test_remove_book_empty_title_raises(self, collection):
        with pytest.raises(BookValidationError, match="Title cannot be empty"):
            collection.remove_book("")

    def test_remove_book_whitespace_only_title_raises(self, collection):
        with pytest.raises(BookValidationError, match="Title cannot be empty"):
            collection.remove_book("   ")
