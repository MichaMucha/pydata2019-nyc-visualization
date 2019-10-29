# download rightmove page -> price, name, location, photo

from typing import Tuple
def get_listing(url:str) -> Tuple[int, str, str, str]:
    return (250_000, 
            'Pretty home', 
            'Richmond, Surrey', 
            'https://unsplash.com/home.png')
