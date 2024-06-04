import socket

def fetch_webpage(url):
    try:
        # Parse URL to get host and path
        url_parts = url.split('/')
        host = url_parts[2]
        path = '/' + '/'.join(url_parts[3:])

        # Create a socket connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the web server
            s.connect((host, 80))
            
            # Send HTTP GET request
            s.sendall(f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n".encode())
            
            # Receive response
            response = b''
            while True:
                data = s.recv(1024)
                if not data:
                    break
                response += data
            
            # Decode response
            response = response.decode('utf-8')
            
            # Extract HTML content (assuming simple content without chunked transfer encoding)
            html_content = response.split('\r\n\r\n', 1)[1]
            
            return html_content
    except Exception as e:
        print("Error:", e)
        return None

def extract_links(html_content):
    # Use simple string manipulation to extract links (not recommended for production)
    links = []
    start_index = 0
    while True:
        # Find start and end index of link tag
        start_tag_index = html_content.find('<a', start_index)
        if start_tag_index == -1:
            break
        end_tag_index = html_content.find('>', start_tag_index)
        
        # Find start and end index of href attribute value
        href_start_index = html_content.find('href="', start_tag_index, end_tag_index)
        if href_start_index == -1:
            break
        href_start_index += 6
        href_end_index = html_content.find('"', href_start_index)
        
        # Extract link
        link = html_content[href_start_index:href_end_index]
        links.append(link)
        
        # Move start_index to end of current link
        start_index = end_tag_index + 1
    
    return links

# URL of the webpage to scrape
url = "http://example.com"

# Fetch the webpage
html_content = fetch_webpage(url)
if html_content:
    # Extract links from the HTML content
    links = extract_links(html_content)
    
    # Print the extracted links
    print("Links found on the webpage:")
    for link in links:
        print(link)
