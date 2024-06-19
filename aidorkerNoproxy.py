import requests
from bs4 import BeautifulSoup
from itertools import cycle
import random

# Function to read queries from a file and append a random number
def get_queries_with_random_number(file_name):
    with open(file_name, 'r') as file:
        queries = [line.strip() + str(random.randint(1, 60)) for line in file]
    return queries

# List of search engines to query.
search_engines = {
    'Google': 'https://www.google.com/search?q=',
    'Bing': 'https://www.bing.com/search?q=',
    'Startpage': 'https://www.startpage.com/do/dsearch?query=',
    'Yahoo': 'https://search.yahoo.com/search?p=',
    'Yandex': 'https://yandex.com/search/?text=',
    # Add more search engines here
}

# Read queries from dorks.txt and append a random number
queries = get_queries_with_random_number('dorks.txt')
urls = []

# Function to read proxies from a file
def get_proxies(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file]

# Read proxies from proxies.txt
#proxy_list = get_proxies('proxies.txt')
    
    # Add more proxies here


# Create a proxy rotation generator
#proxy_pool = cycle(proxy_list)

# List of user agents to simulate different browsers
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-G985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36'
]

# Create a user agent rotation generator
user_agent_pool = cycle(user_agents)

for query in queries:
    for name, base_url in search_engines.items():
       # proxy = next(proxy_pool)
        user_agent = next(user_agent_pool)
        headers = {'User-Agent': user_agent}
        
        try:
            search_response = requests.get(base_url + query, headers=headers)
            soup = BeautifulSoup(search_response.text, 'html.parser')

            # Find all the search result elements. The class names would change based on the search engine.
            if name == 'Google':
                search_results = soup.find_all('div', class_='g')
            elif name == 'Bing':
                search_results = soup.find_all('li', class_='b_algo')
            elif name == 'Startpage':
                search_results = soup.find_all('div', class_='w-gl__result')
            elif name == 'Yahoo':
                search_results = soup.find_all('div', class_='dd algo algo-sr Sr')
            elif name == 'Yandex':
                search_results = soup.find_all('li', class_='serp-item')
            else:
                search_results = []

            # Extract the URLs from the search result elements
            for result in search_results:
                link = result.find('a', href=True)
                if link and "?" in link['href'] and "=" in link['href']:
                    urls.append(link['href'])
        except Exception as e:
            print(f"Error querying {name} with proxy {proxy} and user agent {user_agent}: {e}")

# Remove duplicates and sort the URLs
urls = sorted(set(urls))

# Save the URLs to a text file
with open('search_results.txt', 'w') as file:
    for url in urls:
        file.write(url + '\n')

print(f'Saved {len(urls)} URLs to search_results.txt')
