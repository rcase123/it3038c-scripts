import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.ae.com/us/en/p/men/slim-fit-jeans/athletic-fit-jeans/ae-airflex-athletic-fit-jean/0118_6286_488?menu=cat4840004&ip=off&utm_source=google&utm_medium=pla&utm_content=ae&utm_campaign=nogender_high_general&utm_term=pmax&gad=1&gclid=CjwKCAjw-eKpBhAbEiwAqFL0miugemp63Q4CbVc_4mL4MVmCajuUdCxlL51LrwDjFx9V3EVxPTiSjhoClagQAvD_BwE").content
soup = BeautifulSoup(data, 'html.parser')


title_span = soup.find("div", {"class":"product-sale-price "})
title = title_span

print(f"{title}")