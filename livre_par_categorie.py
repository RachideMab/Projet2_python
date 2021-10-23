import requests
from bs4 import BeautifulSoup
from pprint import pprint
from livre import books_analyse
#from image_url import download_image
from dossier_image import download_image

url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"


#Début de la fonction pour changer de page 
def get_next_page(url):
    next_page = url
    #pprint(next_page)
    next_page_list = []
    next_page_list.append(next_page)
    while True:
        try:

            req = requests.get(next_page)
            page1 = req.content
            soup = BeautifulSoup(page1, "lxml")
            selector = soup.select("li.next")[0].a.get("href")
            #next_page = next[:-10] + selector 
            next_page = url.replace("index.html", selector)
            next_page_list.append(next_page)  
           
        except:
            break
    return next_page_list 
   #Fin de la fonction pour changer de page  

#début de la fonction qui récupère les liens de chaque livre dans une catégorie. 
def book_in_categories(base):
    livres=[]
    for url in get_next_page(base):
        response = requests.get(url)
        page = response.content
        if response.ok:
        
            soup = BeautifulSoup(page, "html.parser")
            titre = "h3"
            titres = soup.find_all('h3')
            for titre in titres:
                a = titre.find('a')
                link = a['href']
                lien = "https://books.toscrape.com/catalogue/" + link[9:]
                book = books_analyse(lien)
                livres.append(book)
                #download_image(book["image_url"], "sf")
                download_image(book["image_url"], 'category')
    return livres
pprint(book_in_categories(url))
#Fin de la fonction qui récupère les liens de chaque livre dans une catégorie. 


