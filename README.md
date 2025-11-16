# News Fetcher

Professional CLI tool for fetching financial news from NewsAPI with filtering and validation.

## What It Does

This tool allows you to:
- Fetch news articles about any topic using NewsAPI
- Display article summaries in a formatted console output
- Save articles to timestamped JSON files for later reference

## Features

### Phase 1 (Basic Functionality)
- ✅ **API Integration**: Connects to NewsAPI to fetch real-time news
- ✅ **JSON Export**: Saves articles with metadata (timestamp, query, article count)
- ✅ **Formatted Output**: Displays article title, author, date, description, and URL
- ✅ **Error Handling**: Graceful handling of API errors and network issues

### Phase 2 (Professional Features)
- ✅ **Professional CLI**: argparse-based command-line arguments
- ✅ **Date Filtering**: Fetch articles from last N days
- ✅ **Data Validation**: Filters out incomplete/removed articles
- ⏳ **Caching**: File-based cache (in progress)

## Requirements

- Python 3.7 or higher
- requests library
- NewsAPI API key (free tier available at https://newsapi.org/)

## Installation

1. Install dependencies:
```bash
pip3 install requests
```

2. Get your free API key from [NewsAPI](https://newsapi.org/)

## Usage

### Phase 2 (Current - Professional CLI)

```bash
# Basic usage (will prompt for API key)
python3 news_fetcher.py --query Tesla

# Specify number of articles
python3 news_fetcher.py --query Bitcoin --count 10

# Filter by date (last 7 days)
python3 news_fetcher.py --query "stock market" --days 7

# Provide API key via command line
python3 news_fetcher.py --query Tesla --api-key YOUR_KEY

# Combine multiple options
python3 news_fetcher.py --query Bitcoin --count 10 --days 7
```

### Command-Line Arguments

- `--query` (required): Search term (e.g., "Tesla", "Bitcoin")
- `--count` (optional): Number of articles to fetch (default: 5)
- `--days` (optional): Fetch articles from last N days
- `--api-key` (optional): NewsAPI key (otherwise prompts)

### Help

```bash
python3 news_fetcher.py --help
```

### Example Output

```
============================================================
  FINANCIAL NEWS FETCHER - DAY 3
============================================================

Enter your NewsAPI key: your-api-key-here
What topic do you want to search? (e.g., 'Tesla', 'Bitcoin'): Tesla

============================================================
📰 FOUND 10 ARTICLES
============================================================

1. Tesla's New Model Released - TechCrunch
Author: John Doe
Published At: 2025-11-07T12:00:00Z
Description: Tesla announces groundbreaking new vehicle...
URL: https://example.com/article

...

Articles saved to 20251107_131834.json

============================================================
✅ DONE!
============================================================
```

## Output File Format

Articles are saved as JSON with the following structure:

```json
{
  "timestamp": "2025-11-07T13:18:34.123456",
  "query": "Tesla",
  "num_articles": 10,
  "articles": [
    {
      "title": "Article Title",
      "author": "Author Name",
      "source": {
        "name": "Source Name"
      },
      "publishedAt": "2025-11-07T12:00:00Z",
      "description": "Article description...",
      "url": "https://example.com/article",
      ...
    }
  ]
}
```

## API Parameters

The fetcher uses these NewsAPI parameters:
- `apiKey`: Your API key
- `q`: Search query
- `pageSize`: Number of articles to fetch
- `sortBy`: Sort by publication date (newest first)
- `language`: English articles only
- `searchIn`: Search in title and description

## Class Structure

### NewsAPIFetcher

**Methods:**
- `__init__(api_key)`: Initialize with API key
- `fetch_articles(query, num_articles=10)`: Fetch articles from API
- `save_articles(articles, filename=None)`: Save to JSON file
- `print_summary(articles)`: Display formatted article list

## Learning Objectives

This project demonstrates:
- Working with RESTful APIs
- HTTP requests with Python's requests library
- JSON data parsing and serialization
- Class-based programming
- Error handling
- User input and command-line interaction
- File I/O operations
- Data formatting and presentation

## Future Enhancements

Potential improvements:
- Store API key in environment variable or config file
- Add command-line arguments for non-interactive use
- Filter by date range
- Support multiple news sources
- Export to other formats (CSV, Excel)
- Add sentiment analysis
- Create web dashboard
- Email digest functionality

## API Rate Limits

Free NewsAPI tier limits:
- 100 requests per day
- 50 articles per request max
- Historical data limited to 30 days

## Project Structure

```
week1-news-fetcher/
├── news_fetcher.py      # Main script
├── README.md            # This file
├── .gitignore          # Git ignore rules
└── *.json              # Output files (timestamped)
```

## License

Educational project for AI learning curriculum.

## Credits

- NewsAPI: https://newsapi.org/
- Python Requests: https://requests.readthedocs.io/

---

## Built

**Phase 1:** Nov 8, 2025 (Week 1, Day 3)
- Approach: 70% manual typing
- Status: ✅ Complete

**Phase 2:** Nov 15, 2025 (Week 1, Day 3 continued)
- Approach: 70% manual typing
- Features: argparse CLI, date filtering, data validation
- Status: ⏳ 75% complete (caching pending)

**Purpose:** Learning API integration, CLI development, and professional Python patterns
