import requests
from bs4 import BeautifulSoup


# URL to copy
url = 'https://www.classcentral.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)

# Make a GET request to the URL
response = result.content.decode()

soup = BeautifulSoup(response, 'html.parser')

# URL to copy
url = 'https://www.classcentral.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)

# Make a GET request to the URL
response = result.content.decode()

soup = BeautifulSoup(response, 'html.parser')





with open('classcentral_copy.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print('Page copied successfully.')