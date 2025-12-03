from collections import deque
import re
from bs4 import BeautifulSoup
import requests
import urllib.parse

print('version 0.1.2  by takaa & authoryvv')

user_url = str(input('[+] Select url: '))
urls = deque([user_url])
scraped_urls = set()
emails = set()
count = 0
limit = int(input('[+] Select your limit: '))

print('_____________________________________________')

try:
    while True:
        count += 1
        if count > limit:
            break

        url = urls.popleft()
        scraped_urls.add(url)

        parts = urllib.parse.urlsplit(url)
        base_url = f'{parts.scheme}://{parts.netloc}'
        path = url[:url.rfind('/')+1] if '/' in parts.path else url

        print(f'{count}. 💀 {url}')

        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
            continue

        new_emails = set(re.findall(r'[a-z0-9\.\-+_]+@\w+\.[a-z\.]+', response.text, re.I))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, 'html.parser')
        for anchor in soup.find_all('a'):
            link = anchor.attrs.get('href', '')

            # Skip url is not falid
            if not link:
                continue
            if link.startswith(("tel:", "mailto:", "javascript:", "#")):
                continue

            # Normalization  link
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link

            # Filter url infalid
            if "://" not in link:
                continue

            if link not in urls and link not in scraped_urls:
                urls.append(link)

except KeyboardInterrupt:
    print('[-] Closing!')

print('\nThat all bro!')
print(f'\n{len(emails)} Email find:')
print('_____________________________________________')

for mail in emails:
    print(' ' + mail)

print('\n')
