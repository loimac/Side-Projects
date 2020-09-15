from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq  

# Url to Scrape
page_url = "https://www.newegg.com/p/pl?d=ram"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds each product
containers = page_soup.findAll("div", {"class": "item-container"})

# name the output file to write to local disk
out_filename = "ram.csv"
# header of csv file to be written
headers = "Brand, Item_name, Shipping_fee, Price \n"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)

# loops over each product and grabs attributes about
# each product
for container in containers:
    div_with_info = container.find('div','item-info').div.select("a")
    brand = div_with_info[0].img["title"].title()
    title_container = container.find('a',"item-title")
    title = title_container.text
    price_container = container.findAll('li',{'class':'price-current'})
    price = price_container[0].strong.text.strip()
    shipping_container = container.findAll('li',{'class': 'price-ship'})
    shipping = shipping_container[0].text.strip()

    # Write to csv file
    f.write(brand + ", " + title.replace(",","|") + "," + shipping + ", $" + price + ".99 " + "\n")

f.close()  # Close the file


