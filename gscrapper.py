#!/usr/bin/env python

import re
import requests
import threading
from bs4 import BeautifulSoup

buscar = 'ice cream'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

r = requests.get('https://www.google.com/search?tbm=shop&hl=en-GB&psb=1&ved=0CAAQvOkFahcKEwigpLCZsf77AhUAAAAAHQAAAAAQCg&gs_ss=1&oq&gs_lcp=Cgtwcm9kdWN0cy1jYxABGAAyCAgAEI8BEOoCMggIABCPARDqAjIICAAQjwEQ6gIyCAgAEI8BEOoCMggIABCPARDqAjIICAAQjwEQ6gIyCAgAEI8BEOoCMggIABCPARDqAjIICAAQjwEQ6gIyCAgAEI8BEOoCUABYAGC9KWgBcAB4AIABAIgBAJIBAJgBALABCg&sclient=products-cc' + '&q=' + buscar.replace(' ', '+'), headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
products = soup.find_all("div", {"class": "sh-dgr__gr-auto sh-dgr__grid-result"})

def process_string(product):
    title = product.h3.decode_contents()
    price = product.find(string=re.compile("\$"))
    imagen = product.img
    print(title, price, imagen)

threads = []
for product in products:
    thread = threading.Thread(target=process_string, args=(product,))
    thread.start()
    # threads.append(thread)

# Wait for all threads to complete
#for thread in threads:
#    thread.join()
