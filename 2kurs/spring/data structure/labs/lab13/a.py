import requests
from bs4 import BeautifulSoup

# Fetch the webpage content
url = "https://textsaver.flap.tv/lists/6fxf"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse XML content
    soup = BeautifulSoup(response.content, "xml")  # Specify "xml" parser for XML content
    
    # Example: Extract dropdown options
    dropdown_options = soup.find_all("option")
    for option in dropdown_options:
        print("Dropdown option:", option.text)
    
    # Example: Extract table data
    table = soup.find("table")
    if table:
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if cells:
                row_data = [cell.text.strip() for cell in cells]
                print("Table row:", row_data)
else:
    print("Failed to fetch webpage:", response.status_code)
