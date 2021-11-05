import requests #pour obtenir les informations du site
from bs4 import BeautifulSoup
from pprint import pprint
import shutil

url = 'https://books.toscrape.com/catalogue/vampire-knight-vol-1-vampire-knight-1_93/index.html'

#Programme d'extraction des données d'un livre sur une page web.

def books_analyse(url: str) -> dict[str, any]: #cette fonction reçoit en entrée une url et nous donne en sortie un dictionnaire. 
   
    response = requests.get(url)
    page = response.content
    soup = BeautifulSoup(page, "lxml")
    title = soup.title.text 
    table = soup.table.find_all('td')
    universal_product_code = table[0].text
    price_including_tax = table[3].text 
    price_excluding_tax = table[2].text
    number_available = table[5].text
    product_description = soup.find_all("p")[3].text
    category = table[1].text 
    review_rating = table[6].text
    image_url = "http://books.toscrape.com" + soup.img['src'][5:]
    book_info = {"Code": universal_product_code, "Title": title, "price_including_tax": price_including_tax, "price_excluding_tax": price_excluding_tax, "number_available": number_available, "product_description": product_description, "category": category, "review_rating": review_rating, "image_url": image_url}
    return book_info
#pprint(books_analyse(url))

