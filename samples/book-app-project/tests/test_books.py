import pytest
from books import BookCollection, BookNotFoundError, BookValidationError


@pytest.fixture()
def collection(tmp_path):
    """Create a BookCollection with temporary storage."""
    temp_file = tmp_path / "data.json"
    temp_file.write_text("[]")
    return BookCollection(data_file=str(temp_file))


def test_add_book(collection):
    initial_count = len(collection.books)
    collection.add_book("1984", "George Orwell", 1949)
    assert len(collection.books) == initial_count + 1
    book = collection.find_by_title("1984")
    assert book is not None
    assert book.author == "George Orwell"
    assert book.year == 1949
    assert book.read is False


def test_add_book_empty_title(collection):
    with pytest.raises(BookValidationError):
        collection.add_book("", "Author", 2020)


def test_add_book_empty_author(collection):
    with pytest.raises(BookValidationError):
        collection.add_book("Title", "  ", 2020)


def test_mark_book_as_read(collection):
    collection.add_book("Dune", "Frank Herbert", 1965)
    result = collection.mark_as_read("Dune")
    assert result is True
    book = collection.find_by_title("Dune")
    assert book.read is True


def test_mark_book_as_read_not_found(collection):
    with pytest.raises(BookNotFoundError):
        collection.mark_as_read("Nonexistent Book")


def test_remove_book(collection):
    collection.add_book("The Hobbit", "J.R.R. Tolkien", 1937)
    result = collection.remove_book("The Hobbit")
    assert result is True
    book = collection.find_by_title("The Hobbit")
    assert book is None


def test_remove_book_not_found(collection):
    with pytest.raises(BookNotFoundError):
        collection.remove_book("Nonexistent Book")


def test_find_by_title_case_insensitive(collection):
    collection.add_book("Dune", "Frank Herbert", 1965)
    assert collection.find_by_title("dune") is not None
    assert collection.find_by_title("DUNE") is not None


def test_find_by_title_not_found(collection):
    assert collection.find_by_title("Nonexistent") is None


def test_find_by_author(collection):
    collection.add_book("1984", "George Orwell", 1949)
    collection.add_book("Animal Farm", "George Orwell", 1945)
    collection.add_book("Dune", "Frank Herbert", 1965)
    results = collection.find_by_author("George Orwell")
    assert len(results) == 2


def test_find_by_author_no_match(collection):
    collection.add_book("1984", "George Orwell", 1949)
    assert collection.find_by_author("Unknown Author") == []


def test_list_books(collection):
    assert collection.list_books() == []
    collection.add_book("1984", "George Orwell", 1949)
    assert len(collection.list_books()) == 1


def test_list_by_year_range(collection):
    collection.add_book("1984", "George Orwell", 1949)
    collection.add_book("Dune", "Frank Herbert", 1965)
    collection.add_book("The Hobbit", "J.R.R. Tolkien", 1937)
    results = collection.list_by_year(1940, 1970)
    assert len(results) == 2
    titles = {b.title for b in results}
    assert titles == {"1984", "Dune"}


def test_list_by_year_no_matches(collection):
    collection.add_book("1984", "George Orwell", 1949)
    results = collection.list_by_year(2000, 2020)
    assert len(results) == 0


def test_list_by_year_single_year(collection):
    collection.add_book("1984", "George Orwell", 1949)
    collection.add_book("Dune", "Frank Herbert", 1965)
    results = collection.list_by_year(1949, 1949)
    assert len(results) == 1
    assert results[0].title == "1984"


def test_list_by_year_reversed_range(collection):
    with pytest.raises(BookValidationError):
        collection.list_by_year(2000, 1900)


def test_list_by_year_empty_collection(collection):
    results = collection.list_by_year(1900, 2000)
    assert len(results) == 0


def test_persistence(tmp_path):
    """Test that data persists across BookCollection instances."""
    temp_file = str(tmp_path / "data.json")
    import json
    with open(temp_file, "w") as f:
        json.dump([], f)

    c1 = BookCollection(data_file=temp_file)
    c1.add_book("1984", "George Orwell", 1949)

    c2 = BookCollection(data_file=temp_file)
    assert len(c2.books) == 1
    assert c2.books[0].title == "1984"


def test_load_missing_file(tmp_path):
    """Missing file results in empty collection, not an error."""
    c = BookCollection(data_file=str(tmp_path / "nonexistent.json"))
    assert c.books == []


def test_load_corrupted_file(tmp_path):
    """Corrupted JSON results in empty collection with warning."""
    bad_file = tmp_path / "data.json"
    bad_file.write_text("{not valid json")
    c = BookCollection(data_file=str(bad_file))
    assert c.books == []
