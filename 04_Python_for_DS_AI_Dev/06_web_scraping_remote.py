import requests
from bs4 import BeautifulSoup

page = requests.get('http://').text

# create BeautifulSoup object
soup = BeautifulSoup(page, 'html.parser')

# pull all instances of <a> tag
artists = soup.find_all('a')

# clear data of all tags
for artist in artists:
    names = artitst.contents[0]
    fullLink = artist.get('href')
    print(names)
    print(fullLink)
