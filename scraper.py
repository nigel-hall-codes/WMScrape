import api
from models import *
from menu import Menu
class Scraper:

    def get_new_dispensaries(self):
        api.download_dispensaries()

    def scrape_menus(self):
        self.get_new_dispensaries()
        dispensaries = Dispensary.select()
        for d in dispensaries:
            m = Menu(d.slug, d._type)
            m.download_menu()


s = Scraper()
s.scrape_menus()