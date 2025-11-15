"""
Financial News Fetcher - Day 3 Project
Fetches news articles from NewsAPI and saves them locally
"""

import requests
import json
from datetime import datetime, timedelta
import time
import argparse

# TODO: Import any other libraries you think you need


class NewsAPIFetcher:
    """
    A class to fetch financial news from NewsAPI.
    
    This is a skeleton - YOU will fill in the logic!
    """
    
    def __init__(self, api_key):
        """
        Initialize the fetcher with your API key.
        
        Args:
            api_key (str): Your NewsAPI key
        """
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/everything"

        # TODO: Add any other attributes you think you'll need
        # Hint: Maybe a list to store articles?
        self.articles = []  # List to store fetched articles
        self.last_query = None  # Store the last search query (optional)
        self.last_fetched_at = None  # Store the time of last fetch (optional)
    
    
    def fetch_articles(self, query, num_articles=5, days=None):
        """
        Fetch articles about a specific topic.
        
        Args:
            query (str): Search term (e.g., "Tesla", "Bitcoin", "banking")
            num_articles (int): How many articles to fetch
            days (int): Fetch articles from last N days (optional)
            
        Returns:
            list: List of article dictionaries
            
        YOUR TASK:
        1. Build the API request URL with parameters
        2. Make the GET request using requests.get()
        3. Check if the request was successful (status code 200)
        4. Parse the JSON response
        5. Return the articles list
        
        HINTS:
        - NewsAPI parameters: apiKey, q (query), pageSize, sortBy
        - Use requests.get(url, params=your_params_dict)
        - Response has JSON with structure: {"articles": [...]}
        - Handle errors with try/except
        """
        try:
            # Build parameters
            params = {
                "apiKey": self.api_key,
                "q": query,
                "pageSize": num_articles,
            }
            #print(f"DEBUG: Param = {params}")
    
            # [2025NOV15] Add date filtering if days is provided
            if days is not None:
                # Calculate the date N days ago using timedelta
                from_date = datetime.now() - timedelta(days=days)
                
                # Format it as ISO 8601 string (YYYY-MM-DD)
                from_date_str = from_date.strftime("%Y-%m-%d")

                # Add to API parameters dict
                params["from"] = from_date_str

                print(f"Filtering articles from {from_date_str} onwards... ")

            # Make API request
            response = requests.get(self.base_url, params=params)
            #print(f"DEBUG: Satus code = {response.status_code}")
            #print(f"DEBUG: Response type = {type(response)}")

            # Check status
            if response.status_code != 200:
                print(f"Error: API returned status {response.status_code}")
                return []

            # Parse JSON
            data = response.json()
            #print(f"DEBUG: Data keys = {data.keys()}")
            
            # Extract articles (safely)
            articles = data.get("articles", [])
            #articles = data["articles"]
            #print(f"DEBUG: Found {len(articles)} articles")

            # # Return results
            # return articles

            # [2025NOV15] Use article validation and filter out invalid articles using list comprehension (Pattern: [item for item in list if condition])
            valid_articles = [article for article in articles if self.is_valid_article(article)]

            # Print how many were filtered out
            filtered_count = len(articles) - len(valid_articles)
            if filtered_count > 0:
                print(f"⚠️ Filtered out {filtered_count} incomplete article(s)")

            # Return only valid articles
            return valid_articles

        except request.exceptions.ConnectionError:
            print("Error: No internet connection!")
            return []
        
        except Exception as e:
            print(f"Error: {e}")
            return []

        pass
    
    # [2025NOV15] Add article validation
    def is_valid_article(self, article):
        """
        Check if an article has all required fields and valid data.

        Args:
            article (dict): Article dictionary from NewsAPI

        Returns:
            bool: True if article is valid, False otherwise
        """

        # Define required fields
        required_fields = ["title", "description", "url", "author"]

        # Check if all required fields exist and are not None
        for field in required_fields:
            value = article.get(field)

            # Check if field is missing or None
            if value is None:
                return False # Invalid!
            
            # Check if field is empty string or "[Removed]"
            if value == "" or value == "[Removed]":
                return False # Invalid!
        
        # If we got here, article is valid!
        return True
    
    def save_articles(self, articles, filename=None):
        """
        Save articles to a JSON file.
        
        Args:
            articles (list): List of article dictionaries
            filename (str): Output filename (optional)
            
        YOUR TASK:
        1. Generate filename if not provided (use timestamp)
        2. Create a data structure to save (include metadata)
        3. Write to JSON file with proper formatting
        
        HINTS:
        - Use datetime.now().strftime("%Y%m%d_%H%M%S") for timestamps
        - json.dump() needs a file handle: open(filename, 'w')
        - Use indent=2 for readable JSON
        """
        
        # TODO: Generate filename if None
        if filename is None:
            # Create filename with timestamp
            filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
        
        # TODO: Prepare data structure
        data = {
            # Add: timestamp, query used, number of articles, articles list
            "timestamp": datetime.now().isoformat(),
            "query": self.last_query if self.last_query else "unknown",
            "num_articles": len(articles),
            "articles": articles
        }
        
        # TODO: Write to file
        try:
            # Open the file in write mode ('w') with the given filename.
            with open(filename, 'w') as f:
                # Serialize the `data` dictionary to JSON format and write it to the file.
                # The 'indent=2' argument makes the JSON output pretty-printed and easy to read.
                json.dump(data, f, indent=2)
            print(f"Articles saved to {filename}")
        except Exception as e:
            print(f"Error saving articles: {e}")
    
    
    def print_summary(self, articles):
        """
        Print a nice summary of fetched articles.
        
        Args:
            articles (list): List of article dictionaries
            
        YOUR TASK:
        Print article information in a readable format.
        Each article has: title, author, publishedAt, description, url
        
        BONUS: Add colors using ANSI codes or emoji for visual appeal!
        """
        
        # TODO: Print header
        print("\n" + "="*60)
        print(f"📰 FOUND {len(articles)} ARTICLES")
        print("="*60 + "\n")
        
        # TODO: Loop through articles and print details
        for i, article in enumerate(articles, 1):
            # Print: number, title, source, date, URL
            # Make it look professional!
            print(f"{i}. {article['title']} - {article['source']['name']}")
            print(f"Author: {article['author']}")
            print(f"Published At: {article['publishedAt']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
            print("\n")


# ============= MAIN PROGRAM =============

# def main():
#     """
#     Main function - this runs when you execute the script.
    
#     YOUR TASK:
#     1. Get API key from user (or config file)
#     2. Get search query from user
#     3. Create NewsAPIFetcher instance
#     4. Fetch articles
#     5. Print summary
#     6. Save to file
#     """
    
#     print("="*60)
#     print("  FINANCIAL NEWS FETCHER - DAY 3")
#     print("="*60)
    
#     # TODO: Get API key
#     # Option 1: From user input
#     # Option 2: From environment variable
#     # Option 3: From config file (better for later)
#     api_key = input("\nEnter your NewsAPI key: ").strip()
    
#     # TODO: Get search query
#     query = input("What topic do you want to search? (e.g., 'Tesla', 'Bitcoin'): ").strip()
    
#     # TODO: Create fetcher instance
#     fetcher = NewsAPIFetcher(api_key)
    
#     # TODO: Fetch articles
#     articles = fetcher.fetch_articles(query, num_articles=5)
    
#     # TODO: Check if we got articles
#     if articles:
#         fetcher.print_summary(articles)
#         fetcher.save_articles(articles)
#     else:
#         print("No articles found.")
    
#     print("\n" + "="*60)
#     print("✅ DONE!")
#     print("="*60)

# [2025NOV15] Rewrite the main() function with argparse
def main():
    """
    Main function with argparse CLI.
    """

    # Create argument parser
    parser = argparse.ArgumentParser(
        description="Fetch financial news from NewsAPI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples: 
    python3 news_fetcher.py --query Tesla --count 5
    python3 news_fetcher.py --query Bitcoin --days 7
    python3 news_fetcher.py --query "stock market" --count 10
        """
    )

    # Add required argument: --query
    parser.add_argument("--query", required=True, help="search query")

    # Add optional argument: --count (default 5)
    parser.add_argument("--count", type=int, default=5, help="number of articles")

    # Add optional argument: --days (we'll use this in Phase 2B)
    parser.add_argument("--days", type=int, help="from last x days")

    # Add optional argument: --api-key
    parser.add_argument("--api-key", help="api-key")

    # Parse arguments
    args = parser.parse_args()

    print("="*60)
    print("  FINANCIAL NEWS FETCHER - PHASE 2")
    print('='*60)

    # Get API key (from args or prompt as fallback)
    api_key = args.api_key if args.api_key else input("Enter your NewsAPI key: ")

    # Create fetcher instance
    fetcher = NewsAPIFetcher(api_key)

    # Fetch articles using args.query and args.count
    articles = fetcher.fetch_articles(args.query, num_articles=args.count, days=args.days)

    # Check if we got articles
    if articles:
        fetcher.print_summary(articles)
        fetcher.save_articles(articles)
    else:
        print("No articles found.")

    print("\n" + "="*60)
    print("✅ DONE!")
    print("="*60)


if __name__ == "__main__":
    main()