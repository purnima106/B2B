# B2B

# B2B Events Scraper

## Requirements
- Python 3.x
- BeautifulSoup
- Requests
- Pandas

## Instructions

1. **Install the required libraries using pip**:
    ```sh
    pip install beautifulsoup4 requests pandas
    ```

2. **Update the `events` list in `scrape_events.py` with actual event URLs**:
    ```python
    events = [
        {
            'name': 'Business Ownership Summit -- Fueling Your Entrepreneurial Spirit',
            'date': 'Sat, Jun 29 • 9:30 PM GMT+5:30',
            'location': '',
            'url': 'https://www.eventbrite.com/e/business-ownership-summit-fueling-your-entrepreneurial-spirit-tickets-1234567890',
            'price': 'Free'
        },
        {
            'name': 'Tender Pipeline: How to plan your bid pipeline for 2024!',
            'date': 'Thu, Jun 27 • 3:30 PM GMT+5:30',
            'location': '',
            'url': 'https://www.eventbrite.com/e/tender-pipeline-how-to-plan-your-bid-pipeline-for-2024-tickets-1234567890',
            'price': 'Free'
        },
        // Add more events here...
    ]
    ```

3. **Run the `scrape_events.py` script**:
    ```sh
    python scrape_events.py
    ```

4. **The output will be saved in `b2b_events.csv`**.

## Summary

This script scrapes the top B2B events and saves the details in a CSV file. It extracts information such as the event name, date, location, description, key speakers, agenda/schedule, registration details, pricing, categories, and audience type.
