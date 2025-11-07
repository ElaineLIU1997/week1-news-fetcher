# Week 1 News Fetcher

A Python script that fetches financial news articles from NewsAPI and saves them to JSON files.

## What It Does

This tool allows you to:
- Fetch news articles about any topic using NewsAPI
- Display article summaries in a formatted console output
- Save articles to timestamped JSON files for later reference

## Features

- **API Integration**: Connects to NewsAPI to fetch real-time news
- **Customizable Search**: Search for any topic (stocks, companies, finance keywords)
- **Article Limit**: Specify how many articles to fetch (default: 10)
- **JSON Export**: Saves articles with metadata (timestamp, query, article count)
- **Formatted Output**: Displays article title, author, date, description, and URL
- **Error Handling**: Graceful handling of API errors and network issues

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

Run the script:
```bash
python3 news_fetcher.py
```

You'll be prompted for:
1. Your NewsAPI key
2. Search topic (e.g., "Tesla", "Bitcoin", "banking")

The script will:
- Fetch the latest 10 articles
- Display a formatted summary
- Save results to a timestamped JSON file

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
