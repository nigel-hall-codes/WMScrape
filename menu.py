import urllib.request
import json
from models import *
import datetime

class Menu:
    def __init__(self, slug, tipe):
        url = 'https://api-g.weedmaps.com/wm/web/v1/listings/{}/menu?type={}'.format(slug, tipe)
        page = urllib.request.urlopen(url)
        data = json.loads(page.read().decode('utf-8'))
        self.data = data
        self.dispensary = Dispensary.get(slug=slug)



    def download_menu(self, t):

        for cat in self.data['categories']:
            catID = cat['menu_item_category_id']
            for item in cat['items']:
                name = item['name']
                product = Product.get_or_create(name=name)

                dhp = DispensaryHasProduct(dispensaryID=self.dispensary.id,
                                           productID=product[0],
                                           date=t)
                dhp.save()
                category_name = item['category_name']
                phc = ProductHasCategory(categoryID=catID,
                                         category=category_name,
                                         productID=product[0])

                prices = item['prices']
                for p in prices:
                    price = Price.get_or_create(amount=p, price=prices[p])
                    print(price)

                    php = ProductHasPrice(priceID=price[0],
                                          productID=product[0],
                                          dispensaryID=self.dispensary.id,
                                          date=t)
                    print(price[0], product[0], self.dispensary.id, t)

                    php.save()




















