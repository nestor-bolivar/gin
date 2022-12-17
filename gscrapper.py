#!/usr/bin/env python

import re
import requests
import json
from bs4 import BeautifulSoup

buscar = 'sega genesis'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

r = requests.get('https://www.google.com/search?tbm=shop&hl=en-GB&psb=1&ved=0CAAQvOkFahcKEwigpLCZsf77AhUAAAAAHQAAAAAQCg&gs_ss=1&oq&gs_lcp=Cgtwcm9kdWN0cy1jYxABGAAyCAgAEI8BEOoCMggIABCPARDqAjIICAAQjwEQ6gIyCAgAEI8BEOoCMggIABCPARDqAjIICAAQjwEQ6gIyCAgAEI8BEOoCMggIABCPARDqAjIICAAQjwEQ6gIyCAgAEI8BEOoCUABYAGC9KWgBcAB4AIABAIgBAJIBAJgBALABCg&sclient=products-cc&q=' + buscar.replace(' ', '+'), headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
products = soup.find_all("div", {"class": "sh-dgr__gr-auto sh-dgr__grid-result"})
# print(soup.prettify())

# for product in (product for product in products):
for product in products:
    gpid = product.get("data-docid") # Google Product ID
    title = product.h3.decode_contents()
    price = product.find(string=re.compile("\$"))
    imagen = product.img.get("src")
    stars = product.find(string=re.compile("out of")) or "No reviews"
    # Known issue with aliexpress
    purl = product.find("a", {"class": "shntl"}).get("href").replace('/url?url=', '').split('%3F', 1)[0]

    # print('####################################')

    value = {
       "gpid": gpid,
       "product": title,
       "price": price,
       "stars": stars,
       "url": purl,
       "img": imagen
     }

    print(json.dumps(value, indent=2))
