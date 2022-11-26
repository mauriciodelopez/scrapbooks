import requests
from bs4 import BeautifulSoup

page = requests.get('https://books.toscrape.com/catalogue/sophies-world_966/index.html')
soup = BeautifulSoup(page.text, 'html.parser')

lists = soup.find_all('article', class_='product_page')
for list in lists:
    title = list.find('h1').text
    price_including_tax = list.find(class_='price_color').text
    price_excluding_tax = list.find(class_='table table-striped_Price (excl. tax)').text
    number_available = list.find(class_='instock availability').text
    #product_description = list.find('p', '...')
    #category
    #review_rating = 
    #image_url
print(price_excluding_tax)  


