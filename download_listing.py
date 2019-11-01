# download browsed rightmove page -> price, name, location, photo
import requests
import bs4
import re
from typing import Tuple

def get_listing(url:str) -> Tuple[int, str, str, str]:
    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.content)
        price = (soup.find('p', attrs={'id': 'propertyHeaderPrice'})
                 .text.strip())
        price = int(re.sub(r'([,£])', '', price))
        return (
            price,
            soup.find('h1', attrs={'itemprop': 'name'}).text,
            soup.find('meta', attrs={'itemprop': 'streetAddress'})['content'],
            soup.find('meta', attrs={'name': 'twitter:image:src'})['content']
        )
    except:
        print('Oops, are you sure about that URL?')
        return (750_000, 
                'Pretty home', 
                'Richmond, Surrey', 
                'https://unsplash.com/home.png')
