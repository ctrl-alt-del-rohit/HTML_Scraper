Title: Nike Product Information Scraper

Description:
The HTML scraper is designed to extract product information from Nike's website. It utilizes the BeautifulSoup library for parsing HTML content and the requests library for making HTTP requests to retrieve web pages.

Functionality:

User-Agent Handling: The scraper allows the specification of a User-Agent string to mimic requests from different devices or browsers, enhancing compatibility and avoiding detection.

HTML Parsing: It uses BeautifulSoup to parse the HTML content of the product pages retrieved from the URLs provided.

Data Extraction: The scraper extracts various product details such as name, price, rating, color, and style from the parsed HTML content.

Error Handling: It includes basic error handling to catch exceptions like value errors when converting scraped data to appropriate formats.

CSV Output: After scraping the product information from all provided URLs, it stores the data in a CSV file with a filename based on the current date.
