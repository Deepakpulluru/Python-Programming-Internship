import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
def fetch_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch webpage content: {response.status_code}")
def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    data = []
    table = soup.find('table')  # Adjust the selector based on your needs
    headers = [header.text for header in table.find_all('th')]
    
    for row in table.find_all('tr')[1:]:  # Skipping the header row
        cells = row.find_all('td')
        row_data = {headers[i]: cells[i].text for i in range(len(cells))}
        data.append(row_data)
    
    return data
def store_data(data, csv_filename, json_filename):
    df = pd.DataFrame(data)
    df.to_csv(csv_filename, index=False)
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
def main(url, csv_filename, json_filename):
    html_content = fetch_webpage(url)
    data = parse_html(html_content)
    store_data(data, csv_filename, json_filename)
    print(f"Data successfully stored in {csv_filename} and {json_filename}")
if __name__ == "__main__":
    url = 'https://example.com'  # Replace with the target URL
    csv_filename = 'data.csv'
    json_filename = 'data.json'
    main(url, csv_filename, json_filename)