import urllib.request
import json
from pprint import pprint

products = []

def get_page(category, page):

    headers = { 'Content-type': 'application/json',
                'Content-length': 0,
                'Accept-Charset': 'UTF-8'}

    url = 'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com' + page

    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req)
    data = json.loads(res.read().decode('utf-8'))

    for product in data['objects']:
        if (product['category'] == category):
            products.append(product)

    if (data['next']):
        return get_page(category, data['next'])

    return products

def avg_cubic_weight(products):
    sum = 0
    for product in products:
        sum +=  (product['size']['width']/100 *
                product['size']['height']/100 *
                product['size']['length']/100) * 250

    return round(sum/len(products),2)


air_cons = get_page('Air Conditioners', '/api/products/1')
weight = avg_cubic_weight(air_cons)

pprint("Average cubic weight is: " + str(weight) + "kg")
