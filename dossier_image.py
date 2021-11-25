import os
import requests # to get image from the web
import shutil # to save it locally

# url_cat= "https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html"
# cat_name = url_cat.split("/")[-2]
# category ='Historical1'
# image_url = "https://books.toscrape.com/media/cache/ec/65/ec651ed66822d4b68938afa645b1ece2.jpg"

def download_image(image_url, cat_name):
    ## Set up the image URL and filename
   
    filename = image_url.split("/")[-1] 

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        #cwd = os.getcwd() 
        if not os.path.exists(cat_name):
             os.mkdir(cat_name)
        path = os.path.abspath(cat_name)
        file = os.path.join(path, filename)
        with open(file,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
       #print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')

# download_image(image_url, cat_name)