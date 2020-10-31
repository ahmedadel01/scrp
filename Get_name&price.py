
from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


my_url = "https://www.jumia.com.eg/smartphones/"
req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req)
wep_page = webpage.read()
webpage.close()

page_soup = soup(wep_page, "html.parser")
# grabs all product
containers_ads = page_soup.find_all("article", {"class":"prd _fb col c-prd"})

filename = "products.csv"
f = open(filename, "w")
headser = "product name, Price\n"
f.write(headser)

for container in containers_ads:
    # title ads
    title_container = container.findAll("h3",{"class": "name"})
    product_name = title_container[0].text.strip()
    # price ads
    price_container = container.findAll("div", {"class": "prc"})
    price = price_container[0].text.strip()
    
    print("product name : " + product_name)
    print("price ads : " + price)
    f.write(product_name + "," + price + "\n")
    
f.close()
