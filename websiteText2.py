import requests
from bs4 import BeautifulSoup

# URL of the webpage with the menu items
url = 'https://hospitality.uoguelph.ca/hours-menus-feedback/daily-menus/creelman-hall-daily-menus'  # Replace with the actual URL

# Fetch the HTML content from the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.text

    # Load HTML content into BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Define the container where menu items are located
    menu_container = soup.find('div', class_='field-items')

    # Check if menu_container is found
    if menu_container:
        # Extract each menu date and associated items
        days = menu_container.find_all('p', class_='rtecenter')
        for day in days:
            # Print day heading (date and/or meal category)
            print(day.text.strip())

            # Following siblings (like <p> and <br>) are the menu items for this day
            for sibling in day.find_next_siblings(['p', 'b']):
                # Stop at a horizontal line or the next date
                if sibling.name == 'hr' or sibling.get('class') == ['rtecenter']:
                    break
                print(" -", sibling.text.strip())
            print("\n" + "="*40 + "\n")
    else:
        print("Menu container not found.")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
