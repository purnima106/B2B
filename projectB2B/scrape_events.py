import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_event_data(event):
    url = event['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    event_data = {
        "Event Name": event['name'],
        "Event Date(s)": event['date'],
        "Location": event.get('location', 'Online'),
        "Website URL": url,
        "Description": "",
        "Key Speakers": [],
        "Agenda/Schedule": [],
        "Registration Details": "",
        "Pricing": event['price'],
        "Categories": [],
        "Audience type": "B2B",
    }

    # Extracting description if present in a specific div
    description_div = soup.find('meta', {'name': 'description'})
    if description_div:
        event_data['Description'] = description_div.get('content', '').strip()

    # Example: Extracting key speakers if present in a specific div
    speakers_div = soup.find_all('div', class_='speaker-name')
    if speakers_div:
        event_data['Key Speakers'] = [speaker.text.strip() for speaker in speakers_div]

    # Example: Extracting agenda/schedule if present in a specific div
    agenda_div = soup.find_all('div', class_='agenda-item')
    if agenda_div:
        event_data['Agenda/Schedule'] = [agenda.text.strip() for agenda in agenda_div]

    # Example: Extracting registration details if present in a specific div
    registration_div = soup.find('div', class_='registration-details')
    if registration_div:
        event_data['Registration Details'] = registration_div.text.strip()

    # Example: Extracting categories if present in a specific div
    categories_div = soup.find_all('div', class_='category')
    if categories_div:
        event_data['Categories'] = [category.text.strip() for category in categories_div]

    return event_data

# List of events with their details and URLs
events = [
    {
        'name': 'Business Ownership Summit -- Fueling Your Entrepreneurial Spirit',
        'date': 'Sat, Jun 29 • 9:30 PM GMT+5:30',
        'location': '',
        'url': 'https://www.eventbrite.com/e/business-ownership-summit-fueling-your-entrepreneurial-spirit-tickets-1234567890',  # Replace with actual URL
        'price': 'Free'
    },
    {
        'name': 'Tender Pipeline: How to plan your bid pipeline for 2024!',
        'date': 'Thu, Jun 27 • 3:30 PM GMT+5:30',
        'location': '',
        'url': 'https://www.eventbrite.com/e/tender-pipeline-how-to-plan-your-bid-pipeline-for-2024-tickets-1234567890',  # Replace with actual URL
        'price': 'Free'
    },
    {
        'name': 'TechCrunch Disrupt 2024',
        'date': 'September 18-20, 2024',
        'location': 'San Francisco, CA',
        'url': 'https://techcrunch.com/events/disrupt-sf-2024/',
        'price': 'Various pricing options'
    },
    {
        'name': 'SaaStr Annual 2024',
        'date': 'September 10-12, 2024',
        'location': 'San Mateo, CA',
        'url': 'https://www.saastrannual.com/',
        'price': 'Various pricing options'
    },
    {
        'name': 'Dreamforce 2024',
        'date': 'September 24-27, 2024',
        'location': 'San Francisco, CA',
        'url': 'https://www.salesforce.com/dreamforce/',
        'price': 'Various pricing options'
    }
]

# Scrape data for each event
scraped_events = []
for event in events:
    scraped_event = scrape_event_data(event)
    scraped_events.append(scraped_event)

# Save the data to a CSV file
df = pd.DataFrame(scraped_events)
df.to_csv('/mnt/data/b2b_events.csv', index=False)

print("Data scraped and saved to b2b_events.csv")
