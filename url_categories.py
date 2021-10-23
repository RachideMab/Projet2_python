import requests
from bs4 import BeautifulSoup
from pprint import pprint

url_site = "https://books.toscrape.com/"

# début de la fonction qui récupère tous les liens des catégories du site. 

def liste_categories(url_site):
    response = requests.get(url_site)
    page = response.content
    if response.ok:
        soup = BeautifulSoup(page, "html.parser")
        side_categories = (soup.findAll('div', attrs={'class':'side_categories'}))[0];
        categories = []
        for anchor_val in side_categories.find_all('a'):
    
            categories.append('https://books.toscrape.com/'+ anchor_val.get('href')[0:])
    
    return categories     
resultat = liste_categories(url_site)
pprint(resultat)

# fin de la fonction qui récupère tous les liens des catégories du site. 
