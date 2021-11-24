import os, csv

#Cette fonction est celle qui permet d'enregistrer les données des livres dans un fichiers csv. 

def save_book_to_csv(liste: list, name: str) -> None:
   
    print(name)
    fichier = name +".csv" 
    for livre in liste:  
        with open(fichier, 'a', newline='', encoding='UTF8') as file:
            writer = csv.DictWriter(file, fieldnames=list(livre.keys()))
            if os.stat(fichier).st_size == 0:
                        # The header is written only if the file is empty
                        writer.writeheader()
            writer.writerow(livre)
                

