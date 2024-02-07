import requests
from bs4 import BeautifulSoup
import re

# URLs of the websites to scrape
urls = [
    "https://hands.ru/company/about/",
    "https://repetitors.info/"
]

# Initialize an empty set to store unique mobile numbers
mobile_numbers = set()

# Iterate over each URL
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = response.text
    
    # Use different regular expressions based on the website
    if url == "https://hands.ru/company/about/":
        numbers = re.findall(r'\+7\s?\(?\d{3}\)?\s?\d{3}[-\s]?\d{2}[-\s]?\d{2}', text)
    else:
        numbers = re.findall(r'8\s?\(?\d{3}\)?\s?\d{3}[-\s]?\d{2}[-\s]?\d{2}', text)
    
    # Add the extracted numbers to the set
    mobile_numbers.update(numbers)

# Print the unique mobile phone numbers
print(mobile_numbers)
