"""
Financial News Fetcher - Day 3 Project
Fetches news articles from NewsAPI and saves them locally
"""

import requests
import json
from datetime import datetime
import time

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
    
    
    def fetch_articles(self, query, num_articles=5):
        """
        Fetch articles about a specific topic.
        
        Args:
            query (str): Search term (e.g., "Tesla", "Bitcoin", "banking")
            num_articles (int): How many articles to fetch
            
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

            # Return results
            return articles

        except request.exceptions.ConnectionError:
            print("Error: No internet connection!")
            return []
        
        except Exception as e:
            print(f"Error: {e}")
            return []

        pass
    
    
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

def main():
    """
    Main function - this runs when you execute the script.
    
    YOUR TASK:
    1. Get API key from user (or config file)
    2. Get search query from user
    3. Create NewsAPIFetcher instance
    4. Fetch articles
    5. Print summary
    6. Save to file
    """
    
    print("="*60)
    print("  FINANCIAL NEWS FETCHER - DAY 3")
    print("="*60)
    
    # TODO: Get API key
    # Option 1: From user input
    # Option 2: From environment variable
    # Option 3: From config file (better for later)
    api_key = input("\nEnter your NewsAPI key: ").strip()
    
    # TODO: Get search query
    query = input("What topic do you want to search? (e.g., 'Tesla', 'Bitcoin'): ").strip()
    
    # TODO: Create fetcher instance
    fetcher = NewsAPIFetcher(api_key)
    
    # TODO: Fetch articles
    articles = fetcher.fetch_articles(query, num_articles=5)
    
    # TODO: Check if we got articles
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