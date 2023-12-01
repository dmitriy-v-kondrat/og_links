import requests
from bs4 import BeautifulSoup


def og_parser(url):
    """
       Extracts Open Graph metadata from a given URL.

       Parameters:
       - url (str): The URL of the webpage from which
        to extract Open Graph metadata.

       Returns:
       dict: A dictionary containing Open Graph metadata.
        Keys represent property names,
         and values are the corresponding content.
    """
    og_dict = {}
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text, 'html.parser')

    if soup.find_all('meta', property=True):
        og = soup.find_all('meta', property=True)
        for i in og:
            og_dict[i.get('property')] = i.get('content')
    else:
        og_dict['og:title'] = soup.title.text
        if soup.find('meta', attrs={'name': "description"}):
            descr = soup.find('meta', attrs={'name': "description"})
            og_dict['og:description'] = descr.get('content')
    return og_dict
