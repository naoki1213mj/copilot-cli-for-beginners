---
name: book-summary
description: Generate a formatted Markdown summary of a book collection from JSON data
---

# Book Summary

Generate a formatted Markdown summary from book collection data (JSON).

## Input

A JSON array of book entries. Each entry has:
- `title` (string) — Book title
- `author` (string) — Author name
- `year` (number) — Publication year
- `read` (boolean) — Whether the book has been read

## Output Format

### 1. Title Section

Start with a heading and total count:

```
# 📚 Book Collection Summary

**Total: N books** | ✅ Read: X | 📖 Unread: Y
```

### 2. Book Table

Output a Markdown table **sorted by year (ascending)** with these columns:

| # | Title | Author | Year | Status |
|---|-------|--------|------|--------|

- **Status column**: Use `✅` for read books, `❌` for unread books
- **Row numbering**: Sequential starting from 1

### 3. Statistics Section

After the table, add a statistics section:

```
## 📊 Statistics

- **Oldest book:** <title> (<year>)
- **Newest book:** <title> (<year>)
- **Reading progress:** X/N (XX%)
```

## Example Output

Given a collection with 4 books (1 read, 3 unread):

```markdown
# 📚 Book Collection Summary

**Total: 4 books** | ✅ Read: 1 | 📖 Unread: 3

| # | Title | Author | Year | Status |
|---|-------|--------|------|--------|
| 1 | The Hobbit | J.R.R. Tolkien | 1937 | ❌ |
| 2 | 1984 | George Orwell | 1949 | ✅ |
| 3 | To Kill a Mockingbird | Harper Lee | 1960 | ❌ |
| 4 | Dune | Frank Herbert | 1965 | ❌ |

## 📊 Statistics

- **Oldest book:** The Hobbit (1937)
- **Newest book:** Dune (1965)
- **Reading progress:** 1/4 (25%)
```

## Rules

- Always sort by year ascending
- Use ✅ for read, ❌ for unread (never text like "Yes"/"No")
- Include all books — do not filter or omit any entries
- If the collection is empty, output: "No books in this collection."
