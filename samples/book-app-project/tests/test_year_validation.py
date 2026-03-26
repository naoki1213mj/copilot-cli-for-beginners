"""Tests for year validation in BookCollection.add_book()."""
from __future__ import annotations
from datetime import datetime
import pytest
from books import BookCollection, BookValidationError


@pytest.fixture()
def collection(tmp_path):
    return BookCollection(data_file=str(tmp_path / "test_books.json"))


class TestYearValidation:
    def test_year_zero_accepted(self, collection):
        book = collection.add_book("Ancient Text", "Unknown", 0)
        assert book.year == 0

    def test_valid_year_accepted(self, collection):
        book = collection.add_book("1984", "George Orwell", 1949)
        assert book.year == 1949

    def test_current_year_accepted(self, collection):
        book = collection.add_book("New Book", "Author", datetime.now().year)
        assert book.year == datetime.now().year

    def test_next_year_accepted(self, collection):
        """Books announced for next year should be accepted."""
        next_year = datetime.now().year + 1
        book = collection.add_book("Upcoming Book", "Author", next_year)
        assert book.year == next_year

    def test_year_too_far_future_rejected(self, collection):
        future = datetime.now().year + 2
        with pytest.raises(BookValidationError, match="cannot be later than"):
            collection.add_book("Future Book", "Author", future)

    def test_negative_year_rejected(self, collection):
        with pytest.raises(BookValidationError, match="cannot be negative"):
            collection.add_book("Bad Book", "Author", -1)

    def test_very_large_negative_year_rejected(self, collection):
        with pytest.raises(BookValidationError, match="cannot be negative"):
            collection.add_book("Bad Book", "Author", -9999)

    def test_very_large_future_year_rejected(self, collection):
        with pytest.raises(BookValidationError, match="cannot be later than"):
            collection.add_book("Far Future", "Author", 9999)
