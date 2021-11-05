import requests
from bs4 import BeautifulSoup
from pprint import pprint
from livre_par_categorie import book_in_categories
from url_categories import liste_categories

url_site = "https://books.toscrape.com/"

#Cette fonction est la fonction principale qui permet de scraper tout le site books.toscrape.com.
#En récupérant les informations de chaque livre de chaque catégorie et les mettant dans un fichier csv.   
def main(url):
    
    for cat in liste_categories(url):
       
        book_in_categories(cat)
   
main(url_site)