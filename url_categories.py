import requests
from bs4 import BeautifulSoup
from pprint import pprint
# from livre_par_categorie import book_in_categories
# url_site = "https://books.toscrape.com/"

# début de la fonction qui récupère tous les liens des catégories du site. 

def liste_categories(url_site):
    response = requests.get(url_site)
    page = response.content
    if response.ok:
        soup = BeautifulSoup(page, "html.parser")
        side_categories = (soup.findAll('div', attrs={'class':'side_categories'}))[0];
        categories = []
        for anchor_val in side_categories.find_all('a')[1:]:
    
            categories.append('https://books.toscrape.com/'+ anchor_val.get('href')[0:])
   
    return categories     
# pprint(liste_categories(url_site)) 
# fin de la fonction qui récupère tous les liens des catégories du site. 

