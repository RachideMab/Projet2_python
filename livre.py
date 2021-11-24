import requests #pour obtenir les informations du site
from bs4 import BeautifulSoup
from pprint import pprint
import shutil

# url = 'https://books.toscrape.com/catalogue/william-shakespeares-star-wars-verily-a-new-hope-william-shakespeares-star-wars-4_871/index.html'

#Programme d'extraction des données d'un livre sur une page web.

def books_analyse(url: str) -> dict[str, any]: #cette fonction reçoit en entrée une url et nous donne en sortie un dictionnaire. 
   
    response = requests.get(url)
    page = response.content
    soup = BeautifulSoup(page, "html.parser")
    title = soup.select("div.product_main>h1")[0].text
    table = soup.table.find_all('td')
    universal_product_code = table[0].text
    price_including_tax = table[3].text 
    price_excluding_tax = table[2].text
    number_available = table[5].text
    product_description = soup.find_all("p")[3].text

    # je récupère la catégorie au niveau des liens de navigation.
    category = soup.select("ul.breadcrumb>li>a")[-1].text
    #category = url.split("/")[-2]
    review_rating = soup.select("p.star-rating")[0].get("class")[-1]
    image_url = "http://books.toscrape.com" + soup.img['src'][5:]
    url_book = url 
    book_info = {"Code": universal_product_code, "Title": title, "url": url_book, "price_including_tax": price_including_tax, "price_excluding_tax": price_excluding_tax, "number_available": number_available, "product_description": product_description, "category": category, "review_rating": review_rating, "image_url": image_url}
    return book_info
# pprint(books_analyse(url))

