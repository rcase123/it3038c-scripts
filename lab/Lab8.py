#importing the plugins
import requests
from bs4 import BeautifulSoup

#This is the website the data is pulled from
data = requests.get("https://www.nike.com/w/mens-shoes-nik1zy7ok").content
#putting the beautiful soup into an attribute
soup = BeautifulSoup(data, 'html.parser')

#scrapping to find title data of the new nike
title_span = soup.find("a", class_= "product-card__link-overlay")
#removing unecessary information from the output
title = title_span.text
#scrapping the cost
cost_span = soup.find("div", class_= "product-price__wrapper css-9xqpgk")
#also removing unecessary data
cost = cost_span.text

#Printing the information
print(f" The New {title} Cost: {cost}")



