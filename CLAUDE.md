# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Context

This is a **learning-focused project** where the developer (Elaine) is building Python skills by typing code herself rather than copying AI-generated solutions. The goal is understanding, not speed.

**Current Status**: Day 3 Phase 1 complete. Phase 2 pending (date filtering, source filtering, argparse CLI, data validation, caching).

**Learning Approach**:
- Developer types 70% of code herself with guidance
- Provide function skeletons with TODO comments, not complete solutions
- Explain concepts; don't just write code
- Encourage debugging before giving answers

## Running the Project

### Basic Usage
```bash
# Install dependencies
pip3 install -r requirements.txt

# Run the fetcher (interactive mode)
python3 news_fetcher.py
```

The script prompts for:
1. NewsAPI key (get free key at https://newsapi.org)
2. Search query (e.g., "Tesla", "Bitcoin")

Output:
- Console summary with formatted article list
- Timestamped JSON file (e.g., `20251107_131834.json`)

### Testing Individual Components
```python
# Test NewsAPIFetcher class
python3 -c "
from news_fetcher import NewsAPIFetcher
fetcher = NewsAPIFetcher('your-api-key')
articles = fetcher.fetch_articles('Tesla', num_articles=5)
print(f'Found {len(articles)} articles')
"
```

## Architecture

### Single-Class Design
The project uses one main class `NewsAPIFetcher` that handles all operations:

1. **Initialization** (`__init__`):
   - Stores API key and base URL
   - Maintains state: `articles`, `last_query`, `last_fetched_at`

2. **Fetching** (`fetch_articles`):
   - Builds NewsAPI request with params: `apiKey`, `q`, `pageSize`
   - Makes GET request to `https://newsapi.org/v2/everything`
   - Handles errors: status codes, network issues
   - Returns article list or empty list on failure

3. **Saving** (`save_articles`):
   - Generates timestamped filename if not provided
   - Creates JSON structure with metadata: timestamp, query, num_articles, articles
   - Writes to file with `indent=2` for readability

4. **Display** (`print_summary`):
   - Formats article data for console output
   - Accesses nested JSON: `article['source']['name']`
   - Uses defensive programming: `.get()` for optional fields

### Data Flow
```
User Input → NewsAPIFetcher → NewsAPI → JSON Response → Parse & Validate → Display → Save
```

### Key Design Patterns

**Defensive Programming**:
```python
# CORRECT (used in code)
articles = data.get("articles", [])  # Returns [] if key missing

# WRONG (causes KeyError)
articles = data["articles"]  # Crashes if key missing
```

**Error Handling Hierarchy**:
1. Specific exceptions first (`ConnectionError`)
2. Generic exceptions last (`Exception`)
3. Always return safe defaults (empty list, not None)

## API Integration Details

### NewsAPI Structure
The fetcher uses NewsAPI v2 "everything" endpoint with these parameters:

**Required**:
- `apiKey`: Authentication (prompted from user)
- `q`: Search query

**Optional** (currently used):
- `pageSize`: Number of articles (default 5)

**Optional** (Phase 2 targets):
- `from`: Date filtering (ISO 8601 format)
- `sources`: Specific outlets (comma-separated)
- `sortBy`: Ordering (currently not set, API defaults to `publishedAt`)
- `language`: Language filter (currently not set)

### Response Structure
```json
{
  "status": "ok",
  "totalResults": 100,
  "articles": [
    {
      "source": {"id": "...", "name": "Source Name"},
      "author": "Author Name",
      "title": "Article Title",
      "description": "Description...",
      "url": "https://...",
      "publishedAt": "2025-11-07T12:00:00Z",
      "content": "Full content..."
    }
  ]
}
```

## Common Development Tasks

### Adding New Parameters
When adding NewsAPI parameters (e.g., date filtering for Phase 2):

1. Add to `params` dict in `fetch_articles()` method (line 64-68)
2. Update docstring to document the parameter
3. Consider making it a method parameter with default value
4. Update README.md API Parameters section

### Handling New Article Fields
When accessing new article fields in `print_summary()`:

1. Use `.get()` for optional fields: `article.get('field', 'default')`
2. Use `[]` only for guaranteed fields: `article['title']`
3. Handle nested structures safely: `article.get('source', {}).get('name', 'Unknown')`

### Phase 2 Implementation Notes

**Date Filtering**:
- Add `from_date` parameter to `fetch_articles()`
- Format as ISO 8601: `datetime.now() - timedelta(days=7)`
- Add to params dict: `"from": from_date.isoformat()`

**Argparse CLI**:
- Replace `input()` calls in `main()` with `argparse.ArgumentParser()`
- Required arg: `--query` or `--topic`
- Optional args: `--days`, `--sources`, `--count`
- API key handling: Try environment variable first, fall back to prompt

**Caching**:
- Check for existing JSON with matching query and recent timestamp
- Compare file timestamp vs current time
- Reuse if < 1 hour old (configurable)

## Learning Context

This project is part of Week 1 AI learning curriculum. The developer is:
- Coming from copy-paste approach (Days 1-2: CSV analyzer)
- Shifting to hands-on typing (Day 3+: News fetcher)
- Building confidence: 3/10 → 6/10 after Phase 1
- Struggling with: Python indentation, try/except, French keyboard `{}`
- Learning: API requests, error handling, JSON structure

**When providing guidance**:
- Give skeletons, not solutions
- Explain the "why" behind code patterns
- Point to documentation rather than writing full implementations
- Let debugging happen (it's part of learning)
- Celebrate understanding over completion
